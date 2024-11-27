import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '7984849829:AAF9Ru8YrSKepje_8McB_a9x6HQmZ6yNvTA'
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я Дон пидиди! Я буду проводить для тебя игры в мафию')

@dp.message()
async def echo(message: types.Message):
    await message.answer(f'Я пока что в разработке так что могу толко показать вам ваше же предложение: {message.text}')

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
