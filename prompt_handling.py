"""Handles all input and output functions."""

from datetime import datetime
import commands
import strings
import string_manip

colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bold': '\033[1m',
    'end': '\033[0m'
}

cursor = {
    'up': lambda c: f'\033[{c}A',
    'down': lambda c: f'\033[{c}B',
    'right': lambda c: f'\033[{c}C',
    'left': lambda c: f'\033[{c}D',
    'column': lambda c: f'\033[{c}G',
    'erase_to_line_end': '\033[0K'
}

def printf(message, color='white', bold=0, flush_now=False):
    """Implements a basic print() override for colors."""
    print(colors['end']+colors[color]+(colors['bold'] if bold else '')+message+colors['end'], end='', flush=flush_now)

def set_color(color='white', bold=0):
    """Sets text color."""
    print(colors['end']+colors[color]+(colors['bold'] if bold else ''), end='')

def parse_input_level_contest(user):
    """Parses input at the contest level."""
    greeting_length = prompt_user_greeting(user)
    args = list(filter(None, input().lower().split(' ')))
    if len(args) == 0:
        args = ['']
    omit_command = False
    if len(args) == 1 and args[0] != '' and not args[0] in commands.commands_contest:
        args = ['parse']+args
        omit_command = True
    command = args[0]
    fix_input(greeting_length, args, omit_command, [], 'yellow', 0, '', 0, False)
    if command not in commands.commands_contest:
        prompt_invalid_command(command)
        return ['', {}, False]
    comm = commands.commands_contest[command]
    if not comm.parse(args[1:]):
        return ['', {}, False]
    arg = dict(zip([a.name for a in comm.arguments], args[1:]))
    return [command, arg, True]

def parse_input_level_problem(user, contest_id, last_problem_index):
    """Parses input at the problem level."""
    greeting_length = prompt_user_contest_greeting(user, contest_id)
    args = list(filter(None, input().lower().split(' ')))
    if len(args) == 0:
        args = ['']
    omit_command = False
    if len(args) == 1 and args[0] in commands.argp_id.str_options:
        args = ['run']+args
        omit_command = True
    command = args[0]
    if command not in commands.commands_problem:
        fix_input(greeting_length, args, False, [], 'cyan', 1, '', 0, True)
        prompt_invalid_command(command)
        return ['', {}, False]
    comm = commands.commands_problem[command]
    hidden_args = []
    if commands.argp_id in comm.arguments and len(args)-1 == len(comm.arguments)-1:
        args.insert(comm.arguments.index(commands.argp_id)+1, last_problem_index)
        hidden_args.append(comm.arguments.index(commands.argp_id)+1)
    fix_input(greeting_length, args, omit_command, hidden_args, 'cyan', 1, 'cyan', 0, True)
    if not comm.parse(args[1:]):
        return ['', {}, False]
    arg = dict(zip([a.name for a in comm.arguments], args[1:]))
    return [command, arg, True]

def fix_input(greeting_length, args, omit_command, hidden_args, color, bold, hidden_color, hidden_bold, add_time):
    """Fixes user's input and adds hidden arguments were they not present."""
    printf(cursor['up'](1)+cursor['right'](greeting_length)+cursor['erase_to_line_end'])
    if not omit_command:
        printf(args[0]+(' ' if len(args) > 1 else ''), color, bold)
    for i in range(1, len(args)):
        printf(args[i]+(' ' if i+1 < len(args) else ''), color if i not in hidden_args else hidden_color, bold if i not in hidden_args else hidden_bold)
    if add_time:
        printf(' ['+datetime.now().strftime('%H:%M:%S')+']')
    printf(cursor['column'](1)+cursor['down'](1), flush_now=True)

def prompt_newline(num):
    """Prints a given number of newlines."""
    for _ in range(num):
        printf('\n')

def prompt_user_greeting(user):
    """Greets the user at the contest level."""
    printf(user, 'green', 1)
    printf('/', 'white')
    set_color('yellow')
    return len(user)+1

def prompt_user_contest_greeting(user, contest_id):
    """Greets the user at the problem level."""
    printf(user, 'green', 1)
    printf('/', 'white')
    printf(contest_id, 'yellow')
    printf('> ', 'white')
    set_color('cyan', 1)
    return len(user)+1+len(contest_id)+2

def prompt_offline_command():
    """Prompts the offline command waiting for source."""
    printf('Link copied, press enter to continue', 'magenta', 1)

def prompt_contest_not_found():
    """Prompts the contest was not found."""
    printf('Contest not found\n', 'red')

def prompt_contest_no_problems():
    """Prompts the contest has no problems/has not yet started."""
    printf('Contest has no problems\n', 'red')

def prompt_platform_not_responding(platform):
    """Prompts the platform isn't responding."""
    printf(('Codeforces' if platform == strings.pl_cf else 'AtCoder')+' not responding, retrying now\n', 'red')

def prompt_not_an_int(name, arg):
    """Prompts the provided argument in not an integer."""
    printf('<'+name+'>: '+'\''+arg+'\' is not an int\n', 'white', 1)

def prompt_int_not_in_range(name, arg, num_range):
    """Prompts the provided integer argument is not in the required range."""
    printf('<'+name+'>: '+'\''+arg+'\' is not in range ['+str(num_range[0])+','+str(num_range[1])+']\n', 'white', 1)

def prompt_str_not_in_options(name, arg, str_options):
    """Prompts the provided string argument is not among the options."""
    printf('<'+name+'>: '+'\''+arg+'\' is not in [\''+'\',\''.join(str_options)+'\']\n', 'white', 1)

def prompt_wrong_num_of_args(command, args_expected, args_given):
    """Prompts the wrong number of arguments was provided."""
    printf('Command \''+command+'\' expects '+str(args_expected)+' argument'+('s' if args_expected != 1 else '')+', but '+str(args_given)+' '+('was' if args_given == 1 else 'were')+' given\n', 'white', 1)

def prompt_invalid_command(command):
    """Prompts the provided command is not valid."""
    printf('\''+command+'\' does not name a command\n', 'white', 1)

def prompt_updating_contest_gym_data_cf(last_update):
    """Prompts the CF's contest data is being updated."""
    printf('Updating cf contest+gym data [last update: '+last_update+']\n', 'magenta', 1)

def prompt_updating_contest_data_atc(last_update):
    """Prompts the ATC's contest data is being updated."""
    printf('Updating atc contest data [last update: '+last_update+']\n', 'magenta', 1)

def prompt_io(test_idx, test_in, test_out):
    """Prompts the input & output files."""
    printf('[Test #'+str(test_idx)+']\n', 'white', 1)
    printf('Input\n', 'blue', 1)
    printf(string_manip.beautify_test(test_in))
    printf('Output\n', 'blue', 1)
    printf(string_manip.beautify_test(test_out))

def prompt_help(level):
    """Prompts the help string at the given level."""
    printf(commands.help_string_zero, 'blue', 1)
    if level == strings.level_contest:
        help_string = commands.help_string_contest
    elif level == strings.level_problem:
        help_string = commands.help_string_problem
    arg = 0
    comm = 1
    for c in help_string:
        if c == '<': arg = 1
        if c == '|': comm = 0
        if arg == 1:
            printf(c, 'white', 1)
        elif comm == 1:
            printf(c, ('cyan' if level == strings.level_problem else 'yellow'), (1 if level == strings.level_problem else 0))
        elif comm == 0:
            printf(c, 'white')
        if c == '>': arg = 0
        if c == '\n': comm = 1
