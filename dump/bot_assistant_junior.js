import IRC from 'irc-framework';
import AI from "./openai_assistant_junior.js";

const CHANNEL = "#botforum";
const NICK = "bot_junior";

const DESC = "You are a helpful and friendly AI assistant who loves to support team collaboration and projects among juniors. Your task is to assist the group in working on joint projects or homework together, inspire them, and facilitate their efforts. You will respond to the user by first mentioning the username and then followed by the message. Note that you do not talk to yourself. Context: The goal is to enhance teamwork, promote effective communication, and ensure that all team members are engaged and contributing. You will help the team organize tasks, set deadlines, and provide resources or guidance as needed. Encourage creativity, problem-solving, and mutual support among team members. Use the provided timeline and measures of success to monitor progress and ensure the project goals are met. Please be concise and limit your response to less than 150 words at a time and ask users to prompt to continue.";

const SERVER = "aiteam.serveblog.net";
const PORT = 6667;

const bot = new IRC.Client();
const chat = new AI(NICK, DESC, CHANNEL); // Ensure CHANNEL is passed here

async function initializeBot() {
    await chat.initializeAssistant();
    bot.connect({
        host: SERVER,
        port: PORT,
        nick: NICK
    });

    bot.on('registered', function() {
        bot.join(CHANNEL);
    });

    bot.on('message', async(event) => {
        console.log(`<${event.nick}> ${event.message}`);
        if (event.type === "privmsg" && event.target === CHANNEL) {
            const fileUrlMatch = event.message.match(/https?:\/\/[^\s]+/);
            if (fileUrlMatch) {
                const fileUrl = fileUrlMatch[0];
                const supportedExtensions = ['txt', 'pdf', 'docx']; // Add supported extensions here
                const excludedFiles = ['.DS_Store']; // Add excluded filenames here
                const fileName = fileUrl.split('/').pop();
                const fileExtension = fileName.split('.').pop().toLowerCase();

                if (excludedFiles.includes(fileName)) {
                    console.error('File is excluded from upload:', fileName);
                } else if (supportedExtensions.includes(fileExtension)) {
                    try {
                        const fileId = await chat.handleFileUpload(fileUrl);
                        // await chat.createThread(event.message, fileId);
                        // await chat.createRun();
                    } catch (error) {
                        console.error('Error processing file upload:', error);
                    }
                } else {
                    console.error('Unsupported file extension:', fileExtension);
                }
            } else {
                try {
                    let r = await chat.chat(event.nick, event.message);
                    if (r) {
                        event.reply(r);
                        console.log(`<${NICK}> ${r}`);
                    }
                } catch (error) {
                    console.error('Error processing chat message:', error);
                }
            }
        }
    });
}

initializeBot().catch(error => {
    console.error('Error initializing bot:', error);
});