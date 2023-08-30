import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Set your OpenAI API key here
openai.api_key = "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"

# Set up the Telegram bot
TOKEN = "6475476761:AAH80Y6_W8i_WJUT8LiI6s8buetiSv2B-XY"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your chatbot. Ask me anything.")

# Function to handle incoming messages
def answer_question(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    # Call the OpenAI API to get a response
    response = openai.Completion.create(
        engine="davinci",  # Choose the appropriate engine
        prompt=user_input,
        max_tokens=50  # Adjust the response length as needed
    )
    bot_response = response.choices[0].text.strip()

    # Send the bot's response back to the user
    update.message.reply_text(bot_response)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Handle /start command
    dispatcher.add_handler(CommandHandler("start", start))

    # Handle user messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer_question))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
