import asyncio
import os

import requests

from loguru import logger

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bs4 import BeautifulSoup
from random import choice
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from handlers.admin_private import admin_router

from common.bot_cmds_list import private

dp = Dispatcher()
CHANNEL_ID = '@fuckyoulolb'

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def main() -> None:
    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}',
               rotation='3 days',
               backtrace=True,
               diagnose=True)
    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    bot.my_admins_list = []
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())

    async def send_random_joke():
        while True:
            try:
                response = requests.get('https://www.anekdot.ru/random/anekdot/')
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jokes = soup.find_all('div', class_='text')

                    random_joke = choice(jokes).text.strip()
                    anekdot = random_joke
                else:
                    anekdot = "Не удалось получить анекдот"

                await bot.send_message(CHANNEL_ID, f"Анекдот: {anekdot}")
                logger.info(f"Опублекован анекдот: {anekdot}")
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения {e}")

            await asyncio.sleep(180)

    task = asyncio.create_task(send_random_joke())

    try:
        await dp.start_polling(bot)
    finally:
        task.cancel()
        await bot.session.close()
        logger.info("Бот остановлен")

if __name__ == "__main__":
    logger.info('Бот запущен')
    asyncio.run(main())
