from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='О нас'),
    KeyboardButton(text="Отправить номер ☎️", request_contact=True),
    KeyboardButton(text="Отправить локацию 🗺️", request_location=True),
)
start_kb.adjust(2, 2)

del_kbd = ReplyKeyboardRemove()
