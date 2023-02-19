import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import main_markup
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"<b>Assalom alaykum {name}\n\n<a href='https://t.me/ustozshogird_clone'>UstozShogird Test</a> kanalining botiga xush kelibsiz!</b>", reply_markup=main_markup)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"<b>Assalom alaykum {name}\n\n<a href='https://t.me/ustozshogird_clone'>UstozShogird Test</a> kanalining botiga xush kelibsiz!</b>", reply_markup=main_markup)

    except Exception as error:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"<b>Assalom alaykum {name}\n\n<a href='https://t.me/ustozshogird_clone'>UstozShogird Test</a> kanalining botiga xush kelibsiz!</b>", reply_markup=main_markup)
        print(error)