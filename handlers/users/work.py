from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.main import confirm_markup
from loader import dp
from states.announcement import Work


@dp.message_handler(text="Ish joyi kerak")
async def create_work_list(message: types.Message):
    await message.answer(text="Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer(text="<b>Ism, familiyangizni kiriting?</b>")
    await Work.full_name.set()


@dp.message_handler(state=Work.full_name)
async def get_worker_full_name(message: types.Message, state: FSMContext):
    await state.update_data({"full_name": message.text})
    await message.answer(text="🕑 Yosh:\n\nYoshingizni kiriting\nMasalan, 19")
    await Work.age.set()


@dp.message_handler(state=Work.age)
async def get_worker_age(message: types.Message, state: FSMContext):
    await state.update_data({"age": message.text})
    await message.answer(text="📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\n<i>Python, C++, C#</i>")
    await Work.technology.set()


@dp.message_handler(state=Work.technology)
async def get_worker_techs(message: types.Message, state: FSMContext):
    try:
        technologies = message.text.split(",")
        text = str()
        if len(technologies) >= 2:
            for tech in technologies:
                text += f"{tech.title()}, "
            await state.update_data({"technologies": text[:-2]})
        elif len(technologies) == 1:
            await state.update_data({"technologies": technologies[0].title()})
    except:
        technologies = message.text
        await state.update_data({"technologies": technologies.title()})
    await message.answer(text="📞 Aloqa:\n\nBog`lanish uchun raqamingizni kiriting\nMasalan, +998 90 123 45 67")
    await Work.phone.set()



@dp.message_handler(state=Work.phone)
async def get_worker_phone(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        phone = ""
    else:
        phone = message.text
    await state.update_data({"phone": phone})
    await message.answer(text="🌐 Hudud:\n\nQaysi hududdansiz\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Work.location.set()


@dp.message_handler(state=Work.location)
async def get_worker_location(message: types.Message, state: FSMContext):
    await state.update_data({"location": message.text})
    await message.answer(text="💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await Work.price.set()


@dp.message_handler(state=Work.price)
async def get_worker_price(message: types.Message, state: FSMContext):
    await state.update_data({"price": message.text})
    await message.answer(text="👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?Masalan, Dasturchi")
    await Work.job.set()


@dp.message_handler(state=Work.job)
async def get_worker_job(message: types.Message, state: FSMContext):
    await state.update_data({"job": message.text})
    await message.answer(text="🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await Work.time.set()
    

@dp.message_handler(state=Work.time)
async def get_worker_time(message: types.Message, state: FSMContext):
    await state.update_data({"time": message.text})
    await message.answer(text="🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering.")
    await Work.goal.set()


@dp.message_handler(state=Work.goal)
async def get_worker_goal(message: types.Message, state: FSMContext):
    await state.update_data({"goal": message.text})
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
    text = f"<b>Ish joyi kerak:</b>\n\n👨‍💼 Xodim: <b>{full_name}</b>\n🕑 Yosh: {age}\n📚 Texnologiya: <b>{technologies}</b>\n🇺🇿 Telegram: @{message.from_user.username}\n📞 Aloqa: <b>{phone}</b>\n🌐 Hudud: <b>{location}</b>\n💰 Narxi: <b>{price}</b>\n👨🏻‍💻 Kasbi: <b>{job}</b>\n🕰 Murojaat qilish vaqti: <b>{time}</b>\n🔎 Maqsad: {goal}"
    await message.answer(text=text)
    await message.answer(text="Barcha ma'lumotlar to'g'rimi?", reply_markup=confirm_markup)
    await Work.confirm.set()

