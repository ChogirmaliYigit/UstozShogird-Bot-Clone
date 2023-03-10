import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import ADMINS
from states.announcement import Partner, Work, Employee, Teacher, Pupil
from keyboards.default.main import main_markup


@dp.callback_query_handler(state=Partner.confirm)
async def get_confirm(call: types.Message, state: FSMContext):
    label = call.data.split("_")[-1]
    data = await state.get_data()
    if label == "true":
        data = await state.get_data()
        full_name = data.get("full_name")
        technologies = data.get("technologies")
        phone = data.get("phone")
        location = data.get("location")
        price = data.get("price")
        job = data.get("job")
        time = data.get("time")
        goal = data.get("goal")
        text = f"<b>Sherik kerak:</b>\n\nπ Sherik: <b>{full_name}</b>\nπ Texnologiya: <b>{technologies}</b>\nπΊπΏ Telegram: @{call.from_user.username}\nπ Aloqa: <b>{phone}</b>\nπ Hudud: <b>{location}</b>\nπ° Narxi: <b>{price}</b>\nπ¨π»βπ» Kasbi: <b>{job}</b>\nπ° Murojaat qilish vaqti: <b>{time}</b>\nπ Maqsad: {goal}"
        user_info = f"User: {call.from_user.full_name}\nTelegram ID: {call.from_user.id}\nIs_bot: {call.from_user.is_bot}\nIs_premium: {call.from_user.is_premium}\nUsername: @{call.from_user.username}\nLanguage code: {call.from_user.language_code}"
        try:
            await bot.send_message(chat_id=-1001897168683, text=text)
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=text)
                await bot.send_message(chat_id=admin, text=user_info)
                await asyncio.sleep(delay=0.05)
        except Exception as error:
            print(error)
        finally:
            await call.message.answer(text="Xabar <a href='https://t.me/chogirmali_yigit'>adminga</a> va <a href='https://t.me/ustozshogird_clone'>kanalga</a> jo'natildi!", reply_markup=main_markup)
            await state.finish()
    elif label == "false":
        await call.message.answer(text="Amaliyot bekor qilindi!", reply_markup=main_markup)
        await state.finish()



@dp.callback_query_handler(state=Work.confirm)
async def get_confirm(call: types.Message, state: FSMContext):
    label = call.data.split("_")[-1]
    data = await state.get_data()
    if label == "true":
        data = await state.get_data()
        full_name = data.get("full_name")
        age = data.get("age")
        technologies = data.get("technologies")
        phone = data.get("phone")
        location = data.get("location")
        price = data.get("price")
        job = data.get("job")
        time = data.get("time")
        goal = data.get("goal")
        text = f"<b>Ish joyi kerak:</b>\n\nπ¨βπΌ Xodim: <b>{full_name}</b>\nπ Yosh: {age}\nπ Texnologiya: <b>{technologies}</b>\nπΊπΏ Telegram: @{call.from_user.username}\nπ Aloqa: <b>{phone}</b>\nπ Hudud: <b>{location}</b>\nπ° Narxi: <b>{price}</b>\nπ¨π»βπ» Kasbi: <b>{job}</b>\nπ° Murojaat qilish vaqti: <b>{time}</b>\nπ Maqsad: {goal}"
        user_info = f"User: {call.from_user.full_name}\nTelegram ID: {call.from_user.id}\nIs_bot: {call.from_user.is_bot}\nIs_premium: {call.from_user.is_premium}\nUsername: @{call.from_user.username}\nLanguage code: {call.from_user.language_code}"
        try:
            await bot.send_message(chat_id=-1001897168683, text=text)
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=text)
                await bot.send_message(chat_id=admin, text=user_info)
                await asyncio.sleep(delay=0.05)
        except Exception as error:
            print(error)
        finally:
            await call.message.answer(text="Xabar <a href='https://t.me/chogirmali_yigit'>adminga</a> va <a href='https://t.me/ustozshogird_clone'>kanalga</a> jo'natildi!", reply_markup=main_markup)
            await state.finish()
    elif label == "false":
        await call.message.answer(text="Amaliyot bekor qilindi!", reply_markup=main_markup)
        await state.finish()


@dp.callback_query_handler(state=Employee.confirm)
async def get_confirm(call: types.Message, state: FSMContext):
    label = call.data.split("_")[-1]
    data = await state.get_data()
    if label == "true":
        data = await state.get_data()
        company_name = data.get("company_name")
        technologies = data.get("technologies")
        phone = data.get("phone")
        location = data.get("location")
        responsible = data.get("responsible")
        time = data.get("time")
        work_time = data.get("work_time")
        salary = data.get("salary")
        extra_info = data.get("extra_info")
        text = f"<b>Xodim kerak:</b>\n\nπ’ Idora: {company_name}\nπ Texnologiya: {technologies}\nπΊπΏ Telegram: @{call.from_user.id}\nπ Aloqa: {phone}\nπ Hudud: {location}\nβοΈ Mas'ul: {responsible}\nπ° Murojaat vaqti: {time}\nπ° Ish vaqti: {work_time}\nπ° Maosh: {salary}\nβΌοΈ Qo`shimcha: {extra_info}"
        user_info = f"User: {call.from_user.full_name}\nTelegram ID: {call.from_user.id}\nIs_bot: {call.from_user.is_bot}\nIs_premium: {call.from_user.is_premium}\nUsername: @{call.from_user.username}\nLanguage code: {call.from_user.language_code}"
        try:
            await bot.send_message(chat_id=-1001897168683, text=text)
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=text)
                await bot.send_message(chat_id=admin, text=user_info)
                await asyncio.sleep(delay=0.05)
        except Exception as error:
            print(error)
        finally:
            await call.message.answer(text="Xabar <a href='https://t.me/chogirmali_yigit'>adminga</a> va <a href='https://t.me/ustozshogird_clone'>kanalga</a> jo'natildi!", reply_markup=main_markup)
            await state.finish()
    elif label == "false":
        await call.message.answer(text="Amaliyot bekor qilindi!", reply_markup=main_markup)
        await state.finish()

@dp.callback_query_handler(state=Teacher.confirm)
async def get_confirm(call: types.Message, state: FSMContext):
    label = call.data.split("_")[-1]
    data = await state.get_data()
    if label == "true":
        data = await state.get_data()
        full_name = data.get("full_name")
        technologies = data.get("technologies")
        phone = data.get("phone")
        location = data.get("location")
        time = data.get("time")
        age = data.get("age")
        job = data.get("job")
        price = data.get("price")
        goal = data.get("goal")
        text = f"<b>Ustoz kerak:</b>\n\nπ Shogird: <b>{full_name}</b>\nπ Yosh: {age}\nπ Texnologiya: <b>{technologies}</b>\nπΊπΏ Telegram: @{call.from_user.username}\nπ Aloqa: <b>{phone}</b>\nπ Hudud: <b>{location}</b>\nπ° Narxi: <b>{price}</b>\nπ¨π»βπ» Kasbi: <b>{job}</b>\nπ° Murojaat qilish vaqti: <b>{time}</b>\nπ Maqsad: {goal}"
        user_info = f"User: {call.from_user.full_name}\nTelegram ID: {call.from_user.id}\nIs_bot: {call.from_user.is_bot}\nIs_premium: {call.from_user.is_premium}\nUsername: @{call.from_user.username}\nLanguage code: {call.from_user.language_code}"
        try:
            await bot.send_message(chat_id=-1001897168683, text=text)
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=text)
                await bot.send_message(chat_id=admin, text=user_info)
                await asyncio.sleep(delay=0.05)
        except Exception as error:
            print(error)
        finally:
            await call.message.answer(text="Xabar <a href='https://t.me/chogirmali_yigit'>adminga</a> va <a href='https://t.me/ustozshogird_clone'>kanalga</a> jo'natildi!", reply_markup=main_markup)
            await state.finish()
    elif label == "false":
        await call.message.answer(text="Amaliyot bekor qilindi!", reply_markup=main_markup)
        await state.finish()


@dp.callback_query_handler(state=Pupil.confirm)
async def get_confirm(call: types.Message, state: FSMContext):
    label = call.data.split("_")[-1]
    data = await state.get_data()
    if label == "true":
        data = await state.get_data()
        full_name = data.get("full_name")
        technologies = data.get("technologies")
        phone = data.get("phone")
        location = data.get("location")
        time = data.get("time")
        age = data.get("age")
        job = data.get("job")
        price = data.get("price")
        goal = data.get("goal")
        text = f"<b>Shogird kerak:</b>\n\nπ Ustoz: {full_name}\nπ Yosh: {age}\nπ Texnologiya: {technologies}\nπΊπΏ Telegram: @{call.from_user.username}\nπ Aloqa: {phone}\nπ Hudud: {location}\nπ° Narxi: {price}\nπ¨π»βπ» Kasbi: {job}\nπ° Murojaat qilish vaqti: {time}\nπ Maqsad: {goal}"
        user_info = f"User: {call.from_user.full_name}\nTelegram ID: {call.from_user.id}\nIs_bot: {call.from_user.is_bot}\nIs_premium: {call.from_user.is_premium}\nUsername: @{call.from_user.username}\nLanguage code: {call.from_user.language_code}"
        try:
            await bot.send_message(chat_id=-1001897168683, text=text)
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=text)
                await bot.send_message(chat_id=admin, text=user_info)
                await asyncio.sleep(delay=0.05)
        except Exception as error:
            print(error)
        finally:
            await call.message.answer(text="Xabar <a href='https://t.me/chogirmali_yigit'>adminga</a> va <a href='https://t.me/ustozshogird_clone'>kanalga</a> jo'natildi!", reply_markup=main_markup)
            await state.finish()
    elif label == "false":
        await call.message.answer(text="Amaliyot bekor qilindi!", reply_markup=main_markup)
        await state.finish()


