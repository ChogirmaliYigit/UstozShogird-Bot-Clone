from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


confirm_markup = InlineKeyboardMarkup(row_width=2)
confirm_markup.insert(InlineKeyboardButton(text="Ha ✅", callback_data="confirm_true"))
confirm_markup.insert(InlineKeyboardButton(text="Yo'q ❌", callback_data="confirm_false"))

