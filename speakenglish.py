
import logging
from aiogram import Bot, Dispatcher, executor, types

from bot import getDefinitions

API_TOKEN = '6657057345:AAFGmXcoebuM_dkQWXkLOaQAQNMdUfIuiz0'

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):


    await message.reply("Lil KD Botiga Xush Kelibsiz!")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Sizga qanday yordam bera olaman?")




@dp.message_handler()
async def handle_message(message: types.Message):
    # Get the word from the message
    word = message.text

    # Get definitions using the getDefinitions function
    definitions = getDefinitions(word)

    # Check if any definitions were found
    if definitions:
        # Construct the response
        response = "\n".join(definitions)
    else:
        response = "No definitions found for the word."

    # Reply with the definitions
    await message.reply(response)

@dp.message_handler()
async def handle_message(message: types.Message):
    # Get the word from the message
    word = message.text

    # Get definitions using the getDefinitions function
    definitions = getDefinitions(word)

    # Construct the response
    response = "\n".join(definitions)

    # Reply with the response
    await message.reply(response)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)