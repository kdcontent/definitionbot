from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(contains='ssalom', ignore_case=True))
@dp.message_handler(Text(equals='Assalomu alaykum', ignore_case=True))
async def text_example(msg: types.Message):
  await msg.reply('Va alaykum assalom')