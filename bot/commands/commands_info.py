from enum import StrEnum


class CommandsCallouts(StrEnum):
    start = "start"
    help = "help"
    play = "play"


bot_commands_description = {
    CommandsCallouts.start: "Объяснение игры",
    CommandsCallouts.help: "Объяснение комманд",
    CommandsCallouts.play: "Играть",
}