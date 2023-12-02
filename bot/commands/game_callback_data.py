import aiogram
from aiogram.filters.callback_data import CallbackData

from entities import Game


class GameCallBackData(CallbackData, prefix="game"):
    text: str
    overallgame: Game
