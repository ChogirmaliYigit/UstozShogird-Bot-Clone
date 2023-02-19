from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text="E'lon joylash uchun /start buyrug'ini tanlang va e'lon berish jarayoni boshidan boshlanadi.")