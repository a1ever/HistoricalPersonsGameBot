from aiogram.filters.callback_data import CallbackData


class BackFactory(CallbackData, prefix="back"):
    where: str


class GameFactory(CallbackData, prefix="game"):
    is_campaign: bool
    is_done: bool
    is_from_game: bool


class MenuFactory(CallbackData, prefix="menu"):
    where: str


class StatisticsFactory(CallbackData, prefix="statistics"):
    where: str


class HelpFactory(CallbackData, prefix="help"):
    where: str


class FactFactory(CallbackData, prefix="fact"):
    where: str
    info: str





