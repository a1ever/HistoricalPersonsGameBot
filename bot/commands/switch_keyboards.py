from contextlib import suppress

from aiogram import types
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import URLInputFile
from sqlalchemy.orm import sessionmaker

from bot.commands.commands_info import game_info
from bot.commands.keyboards.bot_keyboards import get_game_keyboard, get_statistics_keyboard, get_help_keyboard, \
    get_fact_keyboard, generate_round_keyboard
from bot.commands.keyboards.callback_factories import GameFactory, MenuFactory, HelpFactory, StatisticsFactory, \
    FactFactory
from storage.DataBaseAdapter import get_personal_info, get_top_info, get_current_game_state, get_surrender, \
    update_user_in_campaign, create_null_game_state, output_game_state, update_current_game_state, get_user_in_campaign, campaign_status_can


async def callback_menu(callback: types.CallbackQuery,
                        callback_data: MenuFactory, session_maker: sessionmaker) -> None:
    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "play":
                await callback.message.edit_text(callback.message.text,
                                                 reply_markup=await get_game_keyboard(callback.from_user.id, session_maker))
            case "statistics":
                await callback.message.edit_text(callback.message.text, reply_markup=get_statistics_keyboard())
            case "help":
                await callback.message.edit_text(callback.message.text, reply_markup=get_help_keyboard())


async def callback_game(callback: types.CallbackQuery,
                        callback_data: GameFactory, session_maker: sessionmaker) -> None:
    with suppress(TelegramBadRequest):
        await update_user_in_campaign(callback.from_user.id, callback_data.is_campaign, session_maker)
        await create_null_game_state(callback.from_user.id, session_maker)

        await callback.message.edit_text(callback.message.text,
                                             reply_markup=get_fact_keyboard(callback_data.is_done,
                                                                            callback_data.is_from_game,
                                                                            await campaign_status_can(callback.from_user.id,
                                                                                                      session_maker)
                                                                            ))


async def callback_help(callback: types.CallbackQuery,
                        callback_data: HelpFactory, session_maker: sessionmaker) -> None:
    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "game":
                await callback.message.edit_text(text=game_info, reply_markup=get_help_keyboard())
            case "commands":
                await callback.message.edit_text(text="Существует только /start, остальное кнопки",
                                                 reply_markup=get_help_keyboard())


async def callback_statistics(callback: types.CallbackQuery,
                              callback_data: StatisticsFactory, session_maker: sessionmaker) -> None:
    # TODO info in db

    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "self":
                await callback.message.edit_text(text=await get_personal_info(callback.from_user.id, session_maker),
                                                 reply_markup=get_statistics_keyboard())
            case "all":
                await callback.message.edit_text(text=await get_top_info(callback.from_user.id, session_maker),
                                                 reply_markup=get_statistics_keyboard())


async def callback_fact(callback: types.CallbackQuery,
                        callback_data: FactFactory, session_maker: sessionmaker) -> None:
    with suppress(TelegramBadRequest):
        match callback_data.where:
            case "fact":
                ans = await output_game_state(callback.from_user.id, session_maker)
                await callback.message.edit_text(text=ans[0],
                                                 reply_markup=await generate_round_keyboard(callback.from_user.id, session_maker))

            case "surrender":
                await callback.message.edit_text(text=await get_surrender(callback.from_user.id,  session_maker),
                                                 reply_markup=await get_game_keyboard(callback.from_user.id, session_maker))
            case "change":
                await update_user_in_campaign(callback.from_user.id,
                                              not await get_user_in_campaign(callback.from_user.id, session_maker),
                                              session_maker)
                await create_null_game_state(callback.from_user.id, session_maker)
                ans = await output_game_state(callback.from_user.id, session_maker)
                await callback.message.edit_text(text=ans[0],
                                                 reply_markup=await generate_round_keyboard(callback.from_user.id,
                                                                                            session_maker))
            case "game":
                game_state = await get_current_game_state(callback.from_user.id, session_maker)
                match callback_data.info:
                    case "fact":
                        game_state.addFactAmount().addMinus(1)
                        await update_current_game_state(game_state, session_maker)
                        ans = await output_game_state(callback.from_user.id, session_maker)
                        await callback.message.edit_text(text=ans[0],
                                                         reply_markup=await generate_round_keyboard(callback.from_user.id, session_maker, game_state))
                    case "quote":
                        game_state.addQuoteAmount().addMinus(1)
                        await update_current_game_state(game_state, session_maker)
                        ans = await output_game_state(callback.from_user.id, session_maker)
                        await callback.message.edit_text(text=ans[0],
                                                         reply_markup=await generate_round_keyboard(callback.from_user.id, session_maker, game_state))

                    case "age":
                        game_state.addAgeFactAmount().addMinus(5)
                        await update_current_game_state(game_state, session_maker)
                        ans = await output_game_state(callback.from_user.id, session_maker)
                        await callback.message.edit_text(text=ans[0],
                                                         reply_markup=await generate_round_keyboard(callback.from_user.id, session_maker, game_state))
                    case "country":
                        game_state.withDisplayedCountry().addMinus(20)
                        await update_current_game_state(game_state, session_maker)
                        ans = await output_game_state(callback.from_user.id, session_maker)
                        await callback.message.edit_text(text=ans[0],
                                                         reply_markup=await generate_round_keyboard(callback.from_user.id, session_maker, game_state))
                    case "activity":
                        game_state.withDisplayedActivity().addMinus(10)
                        await update_current_game_state(game_state, session_maker)
                        ans = await output_game_state(callback.from_user.id, session_maker)
                        await callback.message.edit_text(text=ans[0],
                                                         reply_markup=await generate_round_keyboard(callback.from_user.id, session_maker, game_state))
                    case "photo":
                        game_state.withDisplayedPhoto().addMinus(50)
                        await update_current_game_state(game_state, session_maker)
                        ans = await output_game_state(callback.from_user.id, session_maker)
                        await callback.message.answer_photo(URLInputFile(ans[1]))
                        await callback.message.edit_text(text=ans[0],
                                                         reply_markup=await generate_round_keyboard(callback.from_user.id, session_maker, game_state))
