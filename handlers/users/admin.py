import aiogram
import asyncio
import pandas as pd
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
from states.announcement import Ads

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[0])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
    else:
       await bot.send_message(message.chat.id, df)
       

@dp.message_handler(text="/optional_ads", user_id=ADMINS)
async def get_ads_content(message: types.Message):
    await message.answer(text="Reklama uchun kontent yuboring")
    await Ads.content.set()

@dp.message_handler(state=Ads.content)
async def send_optional_ads(message: types.Message, state: aiogram.dispatcher.FSMContext):
    users = db.select_all_users()
    for user in users:
        try:
            await message.send_copy(chat_id=user[0])
            await asyncio.sleep(0.05)
        except aiogram.utils.exceptions.ChatNotFound as error:
            pass
    await message.answer(text="Hammaga jo'natildi!")
    await state.finish()

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="@BekoDev, @chogirmali_blog kanallariga obuna bo'ling!")
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
