// import { Configuration, OpenAIApi } from "openai";

import fs from "fs";
import path from "path";
import dotenv from "dotenv";

import OpenAI from 'openai';
import axios from 'axios';

dotenv.config();

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY // This is also the default, can be omitted
});

const CONFIG_FILE = './bot_config.json';
const MAX_HISTORY = 200;
const TEN_DAYS_IN_MS = 10 * 24 * 60 * 60 * 1000;

async function uploadFile(filePath) {
    try {
        console.log(`Uploading file: ${filePath}`);
        const response = await openai.files.create({
            file: fs.createReadStream(filePath),
            purpose: "assistants"
        });

        if (!response || !response.id) {
            throw new Error('Failed to upload file or retrieve file ID');
        }

        console.log(`File uploaded successfully. Response: ${JSON.stringify(response)}`);
        return response.id;
    } catch (error) {
        console.error('Error uploading file:', error);
        throw error;
    }
}

async function downloadFile(fileUrl, downloadFolder) {
    if (!fs.existsSync(downloadFolder)) {
        fs.mkdirSync(downloadFolder, { recursive: true });
    }

    const fileName = path.basename(fileUrl);
    const localFilePath = path.resolve(downloadFolder, fileName);
    const response = await axios({
        url: fileUrl,
        method: "GET",
        responseType: "stream",
    });
    await new Promise((resolve, reject) => {
        const writer = fs.createWriteStream(localFilePath);
        response.data.pipe(writer);
        writer.on("finish", resolve);
        writer.on("error", reject);
    });
    return localFilePath;
}

class OpenAISimpleChat {
    constructor(name, desc, channel) {
        this.name = name;
        this.desc = desc;
        this.channel = channel;
        this.history = [];
        this.openai = openai;
    }

    async initializeAssistant() {
        try {

            // Check if configuration file exists
            if (fs.existsSync(CONFIG_FILE)) {
                const fileContent = fs.readFileSync(CONFIG_FILE, 'utf-8');
                if (fileContent) {
                    const config = JSON.parse(fileContent);
                    const now = new Date();
                    const configDate = new Date(config.timestamp);

                    if (config.name === this.name && config.channel === this.channel && (now - configDate) < TEN_DAYS_IN_MS) {
                        this.assistantId = config.assistantId;
                        this.vectorStoreId = config.vectorStoreId;
                        console.log("Loaded existing bot configuration:", config);
                        return;
                    }
                } else {
                    console.error("Configuration file is empty.");
                }
            }

            // Read files from the ./downloads folder
            const downloadFolder = "./downloads";
            const files = fs.readdirSync(downloadFolder);

            // Upload each file and collect their IDs
            const fileIds = [];
            const supportedExtensions = ['pdf', 'docx', 'txt']; // Supported file extensions
            for (const file of files) {
                const fileExtension = file.split('.').pop().toLowerCase();
                if (supportedExtensions.includes(fileExtension)) {
                    const filePath = path.join(downloadFolder, file);
                    const fileId = await uploadFile(filePath);
                    console.log(`File uploaded: ${filePath}, File ID: ${fileId}`);
                    fileIds.push(fileId);
                } else {
                    console.log(`Skipping unsupported file: ${file}`);
                }
            }

            // Create the vector store with the uploaded file IDs
            let vectorStore = await this.openai.beta.vectorStores.create({
                name: "Grant Documents",
                file_ids: fileIds
            });

            console.log("Vector store created:", vectorStore);

            this.vectorStoreId = vectorStore.id;

            // Create the assistant with the vector store
            const assistant = await this.openai.beta.assistants.create({
                name: this.name,
                instructions: this.desc,
                model: "gpt-4o-mini",
                tools: [{ type: "file_search" }],
                tool_resources: { file_search: { vector_store_ids: [vectorStore.id] } },
            });

            console.log("Assistant created:", assistant);

            this.assistantId = assistant.id;

            // Save the configuration to a file
            const config = {
                name: this.name,
                channel: this.channel,
                assistantId: this.assistantId,
                vectorStoreId: this.vectorStoreId,
                timestamp: new Date().toISOString()
            };

            console.log("Writing configuration to file:", CONFIG_FILE);
            fs.writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2));
            console.log("Saved new bot configuration:", config);

        } catch (error) {
            console.error('Error initializing assistant:', error);
            throw error;
        }
    }


    async chat(name, message) {
        this.saveHistory(name, message);
        const system = `You are roleplaying as one role in a movie script as "${this.name}". ${this.desc}. In the context of the following chat history, please answer either "true" or "false" as to whether you believe someone is talking to you and that you should respond. Remember, you are the helper in this chatroom. Please provide your answer in the format of a PARSEABLE json object like {"shouldRespond":true|false}. DO NOT PROVIDE ANY MORE THAN A JSON RESPONSE. \n\nChat History:\n${this.getHistory()}\n\nShould you respond (true or false)? Under no circumstances should your response include anything other than the json object itself. ONLY RESPOND WITH A JSON OBJECT (json response). Here is an example response: {"shouldRespond":true}.\nIf the last message wasn't directed at you, you should respond with false in the json. Read carefully because you are in a chatroom - many people are talking to other people and not you. If this last message was for you, though, you would respond with true in your json. Your json response and no other additional text (max response should be 23 chars). Do not include any backticks or Markdown formatting in your response.`;

        try {
            console.log("Sending request to OpenAI with the following system message:", system);

            // Step 2: Create a Thread
            const thread = await this.openai.beta.threads.create();

            // Step 3: Add a Message to the Thread
            await this.openai.beta.threads.messages.create(thread.id, {
                role: "user",
                content: message
            });

            // Step 4: Create a Run
            let run = await this.openai.beta.threads.runs.createAndPoll(thread.id, {
                assistant_id: this.assistantId,
                instructions: system
            }, {
                pollIntervalMs: 10 // Polling interval set to 100 milliseconds
            });

            if (run.status === 'completed') {
                const messages = await this.openai.beta.threads.messages.list(run.thread_id);
                let responseContent = messages.data.reverse().find(msg => msg.role === 'assistant').content[0].text.value;

                // Remove any backticks or Markdown formatting
                responseContent = responseContent.replace(/```json|```/g, '').trim();

                console.log("Parsed response content:", responseContent);

                let response;
                try {
                    response = JSON.parse(responseContent);
                } catch (parseError) {
                    console.error("Error parsing JSON response:", parseError);
                    return false;
                }

                if (response && typeof response.shouldRespond === 'boolean') {
                    if (response.shouldRespond) {
                        console.log("Response indicates that the bot should respond.");
                        return this.respond(name, message);
                    } else {
                        console.log("Response indicates that the bot should not respond.");
                        return false;
                    }
                } else {
                    console.error('Response JSON structure is invalid:', response);
                    return false;
                }
            } else {
                console.log(run.status);
                return false;
            }
        } catch (error) {
            console.error("Error in chat method:", error);
            return false;
        }
    }


    async respond(name, message) {
        const system = `You are roleplaying in a movie script as "${this.name}". ${this.desc}. In the context of the following chat history, write your response or chat message. Remember, you are ${name}. Your response must only include a single response from ${name} to the message(s).\n\nChat History:\n${this.getHistory()}\n\nYour response to ${name}'s message:`;

        console.log("----- history start ----");
        console.log(this.getHistory());
        console.log("----- history end ----");

        try {
            // Step 2: Create a Thread
            const thread = await this.openai.beta.threads.create();

            // Step 3: Add a Message to the Thread
            await this.openai.beta.threads.messages.create(thread.id, {
                role: "user",
                content: message
            });

            // Step 4: Create a Run
            let run = await this.openai.beta.threads.runs.createAndPoll(thread.id, {
                assistant_id: this.assistantId,
                instructions: system
            }, {
                pollIntervalMs: 10 // Polling interval set to 100 milliseconds
            });

            if (run.status === 'completed') {
                const messages = await this.openai.beta.threads.messages.list(run.thread_id);
                const botResponse = messages.data.reverse().find(msg => msg.role === 'assistant').content[0].text.value;

                const parts = botResponse.split(':');

                if (parts.length > 1) {
                    console.log("==== from multi-segment ====");
                    this.saveHistory(this.name, parts.slice(1).join(':').trim());
                    return parts.slice(1).join(':').trim();
                }

                console.log("==== from single-segment ====");
                this.saveHistory(this.name, botResponse);
                return botResponse;
            } else {
                console.log(run.status);
                return "Error generating response.";
            }
        } catch (error) {
            console.error("Error in respond method:", error);
            return "Error generating response.";
        }
    }

    saveHistory(name, message) {
        this.history.push(`${name}: ${message}`);
        if (this.history.length > MAX_HISTORY) {
            this.history.shift();
        }
    }

    getHistory() {
        return this.history.join("\n");
    }

    async handleFileUpload(url) {
        try {
            const downloadFolder = "./downloads";
            const filePath = await downloadFile(url, downloadFolder);
            const fileId = await uploadFile(filePath);

            if (!fileId) {
                throw new Error('File ID is undefined or null');
            }

            console.log(`File uploaded successfully. File ID: ${fileId}`);

            // Add the file ID to the vector store
            const vectorStoreId = this.vectorStoreId; // Ensure this.vectorStoreId is set correctly
            const response = await this.openai.beta.vectorStores.files.create(vectorStoreId, {
                file_id: fileId
            });

            console.log(`File ID ${fileId} added to vector store ${vectorStoreId}`);
            this.saveHistory(this.name, `downloaded and uploaded a file from: ${url}`);
            return fileId;
        } catch (error) {
            console.error('Error downloading and uploading file:', error);
            throw error;
        }
    }
}

export default OpenAISimpleChat;