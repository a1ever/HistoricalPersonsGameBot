__all__ = ['register_user_commands', 'bot_commands_description', 'CommandsCallouts']

from aiogram import Router, F
from aiogram.filters import Command

from bot.commands.commands_info import CommandsCallouts, bot_commands_description
from bot.commands.help import command_help
from bot.commands.keyboards.callback_factories import GameFactory, MenuFactory, HelpFactory, StatisticsFactory, FactFactory, BackFactory
from bot.commands.start import command_start, callback_start
from bot.commands.play import command_play, command_answer
from bot.commands.switch_keyboards import callback_game, callback_menu, callback_statistics, callback_help, \
    callback_fact


def register_user_commands(router: Router) -> None:
    router.message.register(command_start, Command(commands=[CommandsCallouts.start]))
    router.message.register(command_start, F.text == 'Правила')
    router.message.register(command_help, Command(commands=[CommandsCallouts.help]))
    router.message.register(command_play, Command(commands=[CommandsCallouts.play]))
    router.callback_query.register(callback_menu, MenuFactory.filter())
    router.callback_query.register(callback_game, GameFactory.filter())
    router.callback_query.register(callback_statistics, StatisticsFactory.filter())
    router.callback_query.register(callback_help, HelpFactory.filter())
    router.callback_query.register(callback_fact, FactFactory.filter())
    router.callback_query.register(callback_start, F.data == "start")
    router.inline_query.register(command_answer)
    # router.callback_query.register()
