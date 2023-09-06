from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp

@dp.message_handler(commands=['language'])
async def changeLang(message: types.Message):
  await message.answer(f"Til o'zgardi")