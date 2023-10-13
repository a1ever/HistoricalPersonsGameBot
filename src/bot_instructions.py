START = 'start'
START_DESCRIPTION = "smth"
HELP = 'help'


COMMANDS_DESCRIPTION = {
    START: START_DESCRIPTION,

}

HELP_DESCRIPTION = '\n\n'.join('/' + key + " \n" + val for key, val in COMMANDS_DESCRIPTION.items())
