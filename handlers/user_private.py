from aiogram import F,  html, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter

from kbdn import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}, я Дон местной мафии")
    await message.answer(f'Хочешь начать игру в мафию?',
                         reply_markup=reply.start_kb.as_markup(
                             resize_keyboard=True,
                             input_feild_placeholder='Что ты хочешь?'))


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer('Меню: ', reply_markup=reply.del_kbd)


@user_private_router.message(or_f(Command("about"), (F.text.lower() == "о нас")))
async def menu_cmd(message: types.Message):
    await message.answer('Привет я разработчик этого прекрасного бота\
 (https://t.me/Kitty2_2_8), этот бот сделан для того чтобы проводить игры в\
 мафию для всей вашей весёлой компании и впринципе чтобы хорошо\
 провести время, если будут какие нибудь вопросы или предложения\
 по функционалу бота то можете написать мне в личку, приятной игры :)')


@user_private_router.message(F.text.lower().contains('52'))
async def menu_cmd(message: types.Message):
    await message.answer('Это второй,\
 52 (алло), да здравствует Санкт-Петербург, и это город наш \
 Я каждый свой новый куплет валю, как никогда\
 Альбом, он чисто мой, никому его не продам (он мой)\
 Не думаю о том, как хорошо было вчера')


@user_private_router.message(F.text)
async def menu_cmd(message: types.Message):
    await message.answer(message.text)


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"номер получен")
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"локация получена")
    await message.answer(str(message.location))
