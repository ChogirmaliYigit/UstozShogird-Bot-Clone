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
        text = f"<b>Sherik kerak:</b>\n\n🏅 Sherik: <b>{full_name}</b>\n📚 Texnologiya: <b>{technologies}</b>\n🇺🇿 Telegram: @{call.from_user.username}\n📞 Aloqa: <b>{phone}</b>\n🌐 Hudud: <b>{location}</b>\n💰 Narxi: <b>{price}</b>\n👨🏻‍💻 Kasbi: <b>{job}</b>\n🕰 Murojaat qilish vaqti: <b>{time}</b>\n🔎 Maqsad: {goal}"
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
        text = f"<b>Ish joyi kerak:</b>\n\n👨‍💼 Xodim: <b>{full_name}</b>\n🕑 Yosh: {age}\n📚 Texnologiya: <b>{technologies}</b>\n🇺🇿 Telegram: @{call.from_user.username}\n📞 Aloqa: <b>{phone}</b>\n🌐 Hudud: <b>{location}</b>\n💰 Narxi: <b>{price}</b>\n👨🏻‍💻 Kasbi: <b>{job}</b>\n🕰 Murojaat qilish vaqti: <b>{time}</b>\n🔎 Maqsad: {goal}"
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
        text = f"<b>Xodim kerak:</b>\n\n🏢 Idora: {company_name}\n📚 Texnologiya: {technologies}\n🇺🇿 Telegram: @{call.from_user.id}\n📞 Aloqa: {phone}\n🌐 Hudud: {location}\n✍️ Mas'ul: {responsible}\n🕰 Murojaat vaqti: {time}\n🕰 Ish vaqti: {work_time}\n💰 Maosh: {salary}\n‼️ Qo`shimcha: {extra_info}"
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
        text = f"<b>Ustoz kerak:</b>\n\n🎓 Shogird: <b>{full_name}</b>\n🕑 Yosh: {age}\n📚 Texnologiya: <b>{technologies}</b>\n🇺🇿 Telegram: @{call.from_user.username}\n📞 Aloqa: <b>{phone}</b>\n🌐 Hudud: <b>{location}</b>\n💰 Narxi: <b>{price}</b>\n👨🏻‍💻 Kasbi: <b>{job}</b>\n🕰 Murojaat qilish vaqti: <b>{time}</b>\n🔎 Maqsad: {goal}"
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
        text = f"<b>Shogird kerak:</b>\n\n🎓 Ustoz: {full_name}\n🌐 Yosh: {age}\n📚 Texnologiya: {technologies}\n🇺🇿 Telegram: @{call.from_user.username}\n📞 Aloqa: {phone}\n🌐 Hudud: {location}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {job}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}"
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


