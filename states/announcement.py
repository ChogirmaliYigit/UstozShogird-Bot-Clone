from aiogram.dispatcher.filters.state import State, StatesGroup


class Partner(StatesGroup):
    full_name = State()
    technology = State()
    phone = State()
    location = State()
    price = State()
    job = State()
    time = State()
    goal = State()
    confirm = State()


class Work(StatesGroup):
    full_name = State()
    age = State()
    technology = State()
    phone = State()
    location = State()
    price = State()
    job = State()
    time = State()
    goal = State()
    confirm = State()


class Employee(StatesGroup):
    company_name = State()
    technology = State()
    phone = State()
    location = State()
    responsible = State()
    time = State()
    work_time = State()
    salary = State()
    extra_info = State()
    confirm = State()


class Teacher(StatesGroup):
    full_name = State()
    age = State()
    technology = State()
    phone = State()
    location = State()
    price = State()
    job = State()
    time = State()
    goal = State()
    confirm = State()


class Pupil(StatesGroup):
    full_name = State()
    age = State()
    technology = State()
    phone = State()
    location = State()
    price = State()
    job = State()
    time = State()
    goal = State()
    confirm = State()
    
class Ads(StatesGroup):
    content = State()