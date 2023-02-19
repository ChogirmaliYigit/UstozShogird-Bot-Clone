from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "@UstozShogirdBot botining clone versiyasi\n\nBu botdagi e'lonlar <a href='https://t.me/ustozshogird_clone'>UstozShogird Test</a> kanaliga test sifatida yuboriladi.\n\n<i><b>MUHIM:</b> botdan hech qanday manfaat ko'zlanmagan!</i>"
    await message.answer(text=text)
