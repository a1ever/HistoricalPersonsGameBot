from aiogram import types
from sqlalchemy.orm import sessionmaker

from bot.commands.commands_info import game_info
from bot.commands.keyboards.bot_keyboards import get_start_keyboard
from storage.DataBaseAdapter import create_new_user


async def command_start(message: types.Message, session_maker: sessionmaker) -> None:
    await create_new_user(message.from_user.id, message.from_user.username, session_maker)
    await message.answer(game_info, reply_markup=get_start_keyboard())


async def callback_start(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(callback.message.text, reply_markup=get_start_keyboard())

