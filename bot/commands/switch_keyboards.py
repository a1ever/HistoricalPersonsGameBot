from contextlib import suppress

from aiogram import types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandObject

from bot.commands.keyboards.bot_keyboards import get_game_keyboard, get_statistics_keyboard, get_help_keyboard, \
    get_fact_keyboard, get_start_keyboard, generate_round_keyboard
from bot.commands.keyboards.callback_factories import GameFactory, MenuFactory, HelpFactory, StatisticsFactory, \
    FactFactory
from storage.DataBaseAdapter import get_personal_info, get_top_info, get_current_fact_state, get_surrender


async def callback_menu(callback: types.CallbackQuery,
        callback_data: MenuFactory) -> None:
    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "play":
                await callback.message.edit_text(callback.message.text, reply_markup=get_game_keyboard())
            case "statistics":
                await callback.message.edit_text(callback.message.text, reply_markup=get_statistics_keyboard())
            case "help":
                await callback.message.edit_text(callback.message.text, reply_markup=get_help_keyboard())


async def callback_game(callback: types.CallbackQuery,
        callback_data: GameFactory) -> None:
    # TODO info in db
    with suppress(TelegramBadRequest):
        match callback_data.is_campaign:
            case True:
                await callback.message.edit_text(callback.message.text, reply_markup=get_fact_keyboard())
            case False:
                await callback.message.edit_text(callback.message.text, reply_markup=get_fact_keyboard())



async def callback_help(callback: types.CallbackQuery,
        callback_data: HelpFactory) -> None:
    # TODO info in db
    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "game":
                await callback.message.edit_text(text="все ж очев", reply_markup=get_help_keyboard())
            case "commands":
                await callback.message.edit_text(text="Существует только /start, остальное кнопки", reply_markup=get_help_keyboard())


async def callback_statistics(callback: types.CallbackQuery,
        callback_data: StatisticsFactory) -> None:
    # TODO info in db

    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "self":
                await callback.message.edit_text(text=await get_personal_info(callback.from_user.id), reply_markup=get_statistics_keyboard())
            case "all":
                await callback.message.edit_text(text=await get_top_info(callback.from_user.id), reply_markup=get_statistics_keyboard())


async def callback_fact(callback: types.CallbackQuery,
        callback_data: FactFactory) -> None:
    # TODO info in db

    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "fact":
                fact = await get_current_fact_state(callback.from_user.id)
                await callback.message.edit_text(text="тут будет что-то да", reply_markup=generate_round_keyboard(fact))
            case "surrender":
                await callback.message.edit_text(text=await get_surrender(callback.from_user.id), reply_markup=get_game_keyboard())

