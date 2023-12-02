from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.commands.keyboards.callback_factories import *
from storage.FactState import Fact


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


def get_game_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Кампания", callback_data=GameFactory(is_campaign=True)
    )
    builder.button(
        text="Один персонаж", callback_data=GameFactory(is_campaign=False)
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


def get_fact_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Получить факт", callback_data=FactFactory(where="fact")
    )
    builder.button(
        text="Сдаюсь", callback_data=FactFactory(where="surrender")
    )

    builder.adjust(1)
    return builder.as_markup()


def generate_round_keyboard(fact: Fact):
    builder = InlineKeyboardBuilder()
    if fact.fact_amount != fact.max_fact_amount:
        builder.button(
            text="Получить", callback_data=FactFactory(where="fact")
        )
    builder.button(
        text="по", callback_data=FactFactory(where="fact")
    )
    builder.button(
        text="ебалу", callback_data=FactFactory(where="surrender")
    )

    builder.adjust(1)
    return builder.as_markup()