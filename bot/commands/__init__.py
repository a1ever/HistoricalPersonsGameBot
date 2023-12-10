__all__ = ['register_user_commands', 'bot_commands_description', 'CommandsCallouts']

from aiogram import Router, F
from aiogram.filters import Command

from bot.commands.commands_info import CommandsCallouts, bot_commands_description
from bot.commands.game_guess import message_guess
from bot.commands.help import command_help
from bot.commands.keyboards.callback_factories import GameFactory, MenuFactory, HelpFactory, StatisticsFactory, \
    FactFactory, BackFactory
from bot.commands.start import command_start, callback_start
from bot.commands.switch_keyboards import callback_game, callback_menu, callback_statistics, callback_help, \
    callback_fact


def register_user_commands(router: Router) -> None:
    router.message.register(command_start, Command(commands=[CommandsCallouts.start]))
    router.message.register(command_help, Command(commands=[CommandsCallouts.help]))
    router.message.register(message_guess, F.text)
    router.callback_query.register(callback_menu, MenuFactory.filter())
    router.callback_query.register(callback_game, GameFactory.filter())
    router.callback_query.register(callback_statistics, StatisticsFactory.filter())
    router.callback_query.register(callback_help, HelpFactory.filter())
    router.callback_query.register(callback_fact, FactFactory.filter())
    router.callback_query.register(callback_start, F.data == "start")
