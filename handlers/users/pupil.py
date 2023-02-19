from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.main import confirm_markup
from loader import dp
from states.announcement import Pupil


@dp.message_handler(text="Shogird kerak")
async def create_pupil_list(message: types.Message):
    await message.answer(text="Shogird topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer(text="<b>Ism, familiyangizni kiriting</b>")
    await Pupil.full_name.set()


@dp.message_handler(state=Pupil.full_name)
async def get_pupil_full_name(message: types.Message, state: FSMContext):
    await state.update_data({"full_name": message.text})
    await message.answer(text="🕑 Yosh:\n\nYoshingizni kiriting\nMasalan, 19")
    await Pupil.age.set()


@dp.message_handler(state=Pupil.age)
async def get_pupil_age(message: types.Message, state: FSMContext):
    await state.update_data({"age": message.text})
    await message.answer(text="📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\n<i>Python, C++, C#</i>")
    await Pupil.technology.set()


@dp.message_handler(state=Pupil.technology)
async def get_pupil_techs(message: types.Message, state: FSMContext):
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
    await Pupil.phone.set()


@dp.message_handler(state=Pupil.phone)
async def get_pupil_phone(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        phone = ""
    else:
        phone = message.text
    await state.update_data({"phone": phone})
    await message.answer(text="🌐 Hudud:\n\nQaysi hududdansiz\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Pupil.location.set()


@dp.message_handler(state=Pupil.location)
async def get_pupil_location(message: types.Message, state: FSMContext):
    await state.update_data({"location": message.text})
    await message.answer(text="💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await Pupil.price.set()


@dp.message_handler(state=Pupil.price)
async def get_pupil_price(message: types.Message, state: FSMContext):
    await state.update_data({"price": message.text})
    await message.answer(text="👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?Masalan, Dasturchi")
    await Pupil.job.set()



@dp.message_handler(state=Pupil.job)
async def get_pupil_job(message: types.Message, state: FSMContext):
    await state.update_data({"job": message.text})
    await message.answer(text="🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await Pupil.time.set()


@dp.message_handler(state=Pupil.time)
async def get_pupil_time(message: types.Message, state: FSMContext):
    await state.update_data({"time": message.text})
    await message.answer(text="🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering.")
    await Pupil.goal.set()


@dp.message_handler(state=Pupil.goal)
async def get_pupil_goal(message: types.Message, state: FSMContext):
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
    text = f"<b>Shogird kerak:</b>\n\n🎓 Ustoz: {full_name}\n🌐 Yosh: {age}\n📚 Texnologiya: {technologies}\n🇺🇿 Telegram: @{message.from_user.username}\n📞 Aloqa: {phone}\n🌐 Hudud: {location}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {job}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}"
    await message.answer(text=text)
    await message.answer(text="Barcha ma'lumotlar to'g'rimi?", reply_markup=confirm_markup)
    await Pupil.confirm.set()


