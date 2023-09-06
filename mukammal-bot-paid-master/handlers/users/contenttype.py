from aiogram import types
from aiogram.dispatcher import filters
from loader import dp


@dp.message_handler(content_types=['photo'])
async def photo_handler(msg: types.Message):
  await msg.answer(f'Bu nima?')

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(msg: types.Message):
  await msg.answer(f'Bu kim?')

@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def sticker_handler(msg: types.Message):
  await msg.answer(f'Bu nima?')
@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtag_example(msg:types.Message):
  await msg.answer('Yeee, akang kuchaydi')
