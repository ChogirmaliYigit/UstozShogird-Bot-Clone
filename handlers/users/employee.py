from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.main import confirm_markup
from loader import dp
from states.announcement import Employee



@dp.message_handler(text="Xodim kerak")
async def create_vacancy_list(message: types.Message):
    await message.answer(text="Xodim topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer(text="🎓 Idora nomi?")
    await Employee.company_name.set()


@dp.message_handler(state=Employee.company_name)
async def get_company_name(message: types.Message, state: FSMContext):
    await state.update_data({"company_name": message.text})
    await message.answer(text="📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\n<i>Python, C++, C#</i>")
    await Employee.technology.set()


@dp.message_handler(state=Employee.technology)
async def get_company_techs(message: types.Message, state: FSMContext):
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
    await Employee.phone.set()


@dp.message_handler(state=Employee.phone)
async def get_company_phone(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        phone = ""
    else:
        phone = message.text
    await state.update_data({"phone": phone})
    await message.answer(text="🌐 Hudud:\n\nQaysi hududdansiz\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Employee.location.set()


@dp.message_handler(state=Employee.location)
async def get_company_location(message: types.Message, state: FSMContext):
    await state.update_data({"location": message.text})
    await message.answer(text="✍️Mas'ul ism sharifi?")
    await Employee.responsible.set()


@dp.message_handler(state=Employee.responsible)
async def get_company_responsible(message: types.Message, state: FSMContext):
    await state.update_data({"responsible": message.text})
    await message.answer(text="🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await Employee.time.set()


@dp.message_handler(state=Employee.time)
async def get_company_time(message: types.Message, state: FSMContext):
    await state.update_data({"time": message.text})
    await message.answer(text="🕰 Ish vaqtini kiriting?")
    await Employee.work_time.set()


@dp.message_handler(state=Employee.work_time)
async def get_company_work_time(message: types.Message, state: FSMContext):
    await state.update_data({"work_time": message.text})
    await message.answer(text="💰 Maoshni kiriting?")
    await Employee.salary.set()


@dp.message_handler(state=Employee.salary)
async def get_company_salary(message: types.Message, state: FSMContext):
    await state.update_data({"salary": message.text})
    await message.answer(text="‼️ Qo`shimcha ma`lumotlar?")
    await Employee.extra_info.set()


@dp.message_handler(state=Employee.extra_info)
async def get_company_extra_infos(message: types.Message, state: FSMContext):
    await state.update_data({"extra_info": message.text})
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
    text = f"<b>Xodim kerak:</b>\n\n🏢 Idora: {company_name}\n📚 Texnologiya: {technologies}\n🇺🇿 Telegram: @{message.from_user.id}\n📞 Aloqa: {phone}\n🌐 Hudud: {location}\n✍️ Mas'ul: {responsible}\n🕰 Murojaat vaqti: {time}\n🕰 Ish vaqti: {work_time}\n💰 Maosh: {salary}\n‼️ Qo`shimcha: {extra_info}"
    await message.answer(text=text)
    await message.answer(text="Barcha ma'lumotlar to'g'rimi?", reply_markup=confirm_markup)
    await Employee.confirm.set()

