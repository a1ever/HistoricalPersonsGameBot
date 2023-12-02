from aiogram import types
from aiogram.filters import CommandObject
from bot.commands import bot_commands_description, CommandsCallouts


async def command_help(message: types.Message, command: CommandObject):
    if command.args:
        return await message.answer("На данный момент бот не может выдать справку по конкретной команде")
    return await message.answer(bot_commands_description[CommandsCallouts.help])
