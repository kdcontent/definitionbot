from aiogram import types
from aiogram.dispatcher.filters import Regexp
from loader import dp

EMAIL = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUMBER = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

@dp.message_handler(Regexp(EMAIL))
async def regexp_email(msg: types.Message):
  await msg.answer('Email qabul qilindi')

@dp.message_handler(Regexp(PHONE_NUMBER))
async def regexp_phone_number(msg: types.Message):
  await msg.answer('Telefon raqam qabul qilindi')