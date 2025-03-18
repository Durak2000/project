from loguru import logger
from aiogram import F,  html, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter

from kbdn.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    logger.info(f'Пользователь {(message.from_user.full_name)}, запустил бота')
    await message.answer(f"Здравствуйте,\
 {html.bold(message.from_user.full_name)},\
 я помогу вам сделать ваш праздник веселее и красивее")
    await message.answer(
        "Привет, я виртуальный помощник",
        reply_markup=get_keyboard(
            "Меню",
            "О нас",
            "Отправить номер ☎️",
            "Отправить локацию 🗺️",
            placeholder="Что вас интересует?",
            sizes=(2, 2)
        ),
    )


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer(
        "Вот меню:",
        reply_markup=get_keyboard(
            "Каталог",
            "Варианты оплаты",
            "Варианты доставки",
            placeholder="Что вас интересует?",
            sizes=(1, 2)
        ),
    )


@user_private_router.message(or_f(Command("about"), (F.text.lower() == "о нас")))
async def menu_cmd(message: types.Message):
    await message.answer('Добрый день! Предлагаем гелиевые шары с обработкой\
 HI-Float и без с доставкой на дом на радостное событие в Вашей жизни на Дни\
 Рождения, мероприятия, на выписку, да и просто поднять настроение любимым!!!')


# @user_private_router.message(F.text)
# async def menu_cmd(message: types.Message):
#     await message.answer(message.text)


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer("номер получен")
    logger.info(message.contact)


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer("локация получена")
    logger.info(message.location)
    await message.answer(str(message.location))
