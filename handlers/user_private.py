from aiogram import html, types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}, я Дон местной мафии")
    await message.answer(f'Хочешь начать игру в мафию?') 

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Бот пока что в разработке')
    await message.answer('Так что давай не наглей')
