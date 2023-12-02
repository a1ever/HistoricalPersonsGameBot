from aiogram import types

from bot.commands.keyboards.bot_keyboards import get_start_keyboard
from services.json_service import GetRandomPerson


async def command_start(message: types.Message) -> None:
    pers = await GetRandomPerson()
    await message.answer(f"{pers.Name}: \n {pers.GetRandomFact()}\n {pers.GetRandomAgeFact()}", reply_markup=get_start_keyboard())


async def callback_start(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(callback.message.text, reply_markup=get_start_keyboard())

