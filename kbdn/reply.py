from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='О нас'),
)
start_kb.adjust(1, 1)

del_kbd = ReplyKeyboardRemove()
