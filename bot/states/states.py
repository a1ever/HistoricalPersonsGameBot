from aiogram.fsm.state import StatesGroup, State


class Guess(StatesGroup):
    waiting_for_guess = State()
    waiting_for_surrender = State()

