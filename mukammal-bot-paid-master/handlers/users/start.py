from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
@dp.message_handler(CommandStart(deep_link=['kunuz']))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f'Salom, {message.from_user.full.name}!'
    text += f'Sizni {args} tavsiya qildi'
    await message.answer(text)
