from typing import Optional

from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.orm import sessionmaker

from bot.commands.keyboards.callback_factories import *
from storage.DataBaseAdapter import get_current_game_state, get_user_in_campaign, \
    campaign_status_can
from storage.Models.game_state_model import GameStateModel
from storage.db import Fact, GameState


def get_start_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Играть", callback_data=MenuFactory(where="play")
    )
    builder.button(
        text="Статистика", callback_data=MenuFactory(where="statistics")
    )
    builder.button(
        text="Справка", callback_data=MenuFactory(where="help")
    )

    builder.adjust(1)
    return builder.as_markup()


async def get_game_keyboard(user_id: int, session_maker: sessionmaker):
    builder = InlineKeyboardBuilder()
    if await campaign_status_can(user_id, session_maker):
        builder.button(
            text="Кампания", callback_data=GameFactory(is_campaign=True, is_done=False, is_from_game=False)
        )
    builder.button(
        text="Один персонаж", callback_data=GameFactory(is_campaign=False, is_done=False, is_from_game=False)
    )
    builder.button(
        text="Назад", callback_data="start"
    )

    builder.adjust(1)
    return builder.as_markup()


def get_statistics_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Личная статистика", callback_data=StatisticsFactory(where="self")
    )
    builder.button(
        text="Рейтинг среди пользователей", callback_data=StatisticsFactory(where="all")
    )
    builder.button(
        text="Назад", callback_data="start"
    )

    builder.adjust(1)
    return builder.as_markup()


def get_help_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Об игре", callback_data=HelpFactory(where="game")
    )
    builder.button(
        text="О командах", callback_data=HelpFactory(where="commands")
    )
    builder.button(
        text="Назад", callback_data="start"
    )

    builder.adjust(1)
    return builder.as_markup()


def get_fact_keyboard(is_done: bool, is_from_game: bool, can_change: bool):
    builder = InlineKeyboardBuilder()
    if not is_done:
        builder.button(
            text="Получить факт в текущей игре", callback_data=FactFactory(where="fact", info="")
        )
    if is_from_game:
        if can_change:
            builder.button(
                text="Изменить режим игры", callback_data=FactFactory(where="change", info="")
            )
        builder.button(
            text="Сдаюсь в текущей игре", callback_data=FactFactory(where="surrender", info="")
        )

    builder.adjust(1)
    return builder.as_markup()


async def generate_round_keyboard(user_id: int, session_maker: sessionmaker,
                                  game_state: Optional[GameStateModel] = None):
    if game_state is None:
        game_state = await get_current_game_state(user_id, session_maker)
    builder = InlineKeyboardBuilder()
    if game_state.fact_amount < 10:
        builder.button(
            text="Получить факт", callback_data=FactFactory(where="game", info="fact")
        )

    if game_state.quote_amount < 5:
        builder.button(
            text="Получить цитату", callback_data=FactFactory(where="game", info="quote")
            #     game_state=game_state
            #                                                               .withNewQuoteAmount(game_state.fact_amount + 1)
            #                                                               .addMinus(1)
        )
    if game_state.age_fact_amount < 2:
        builder.button(
            text="Факт о возрасте", callback_data=FactFactory(where="game", info="age")
            #    game_state=game_state
            #                                                                        .withNewAgeFactAmount(game_state.fact_amount + 1)
            #                                                                        .addMinus(3)
        )
    if not game_state.displayed_country:
        builder.button(
            text="Откуда родом?", callback_data=FactFactory(where="game", info="country")
            #     game_state=game_state
            #                                                             .withDisplayedCountry()
            #                                                             .addMinus(5)
        )
    if not game_state.displayed_photo:
        builder.button(
            text="Фото", callback_data=FactFactory(where="game", info="photo")
            # game_state=game_state   .withDisplayedCountry()                     .addMinus(10)
        )
    if not game_state.displayed_activity:
        builder.button(
            text="Вид деятельности", callback_data=FactFactory(where="game", info="activity")
            #     game_state
            #                                                                .withDisplayedCountry()
            #                                                                .addMinus(10)
        )
    builder.button(
        text="Назад", callback_data=GameFactory(is_campaign=await get_user_in_campaign(user_id, session_maker),
                                                is_done=game_state.is_done(), is_from_game=True))
    builder.adjust(2)
    return builder.as_markup()
