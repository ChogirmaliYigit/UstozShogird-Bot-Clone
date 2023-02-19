from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_markup.row("Sherik kerak", "Ish joyi kerak")
main_markup.row("Xodim kerak", "Ustoz kerak")
main_markup.row("Shogird kerak")

