from aiogram import F,  html, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}, я Дон местной мафии")
    await message.answer(f'Хочешь начать игру в мафию?') 

@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer('Бот пока что в разработке')
    await message.answer('Так что давай не наглей')

@user_private_router.message(Command('about'))
async def menu_cmd(message: types.Message):
    await message.answer('Привет я разработчик этого прекрасного бота\
 (https://t.me/Kitty2_2_8), этот бот сделан для того чтобы проводить игры в\
 мафию для всей вашей весёлой компании и впринципе чтобы хорошо провести время,\
 если будут какие нибудь вопросы или предложения по функционалу бота то можете написать мне в личку, приятной игры :)')

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

@user_private_router.message(F.audio)
async def menu_cmd(message: types.Message):
    await message.answer('Ты че вообще куку боту гс присылать?')