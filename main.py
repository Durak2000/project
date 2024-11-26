import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '7908811468:AAF2eRhhiROPR0DJ9xOGeHZIunE4aTwsnKE'
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я Дон пидиди! Я буду проводить для тебя игры в мафию')

@dp.message()
async def echo(message: types.Message):
    await message.answer(f'если в твоем сообшение: {message.text} есть что то оскорбительное то сам такой, чорт паганый')

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
