import colorama
import commands
import strings

def init():
    colorama.init()

colors={
    'black':'\033[30m',
    'red':'\033[31m',
    'green':'\033[32m',
    'yellow':'\033[33m',
    'blue':'\033[34m',
    'magenta':'\033[35m',
    'cyan':'\033[36m',
    'white':'\033[37m',
    'bold':'\033[1m',
    'end':'\033[0m'
}

def printf(message,color='white',bold=0):
    print(colors['end']+colors[color]+(colors['bold'] if bold else '')+message+colors['end'],end='')

def set_color(color='white',bold=0):
    print(colors['end']+colors[color]+(colors['bold'] if bold else ''),end='')


def prompt_newline(num):
    for i in range(num):
        printf('\n')

def prompt_user(user):
    printf(user,'green',1)
    printf('/','white')
    set_color('yellow')

def prompt_user_contest(user,contest_id):
    printf(user,'green',1)
    printf('/','white')
    printf(contest_id,'yellow')
    printf('> ','white')
    set_color('cyan',1)

def prompt_contest_not_found():
    printf('Contest not found\n','red')

def prompt_contest_no_problems():
    printf('Contest has no problems\n','red')

def prompt_platform_not_responding(platform):
    printf(('Codeforces' if platform=='cf' else 'AtCoder')+' not responding, retrying now\n','red')

def prompt_not_an_int(name,arg):
    printf('<'+name+'>: '+'\''+arg+'\' is not an int\n','white',1)

def prompt_int_not_in_range(name,arg,num_range):
    printf('<'+name+'>: '+'\''+arg+'\' is not in range ['+str(num_range[0])+','+str(num_range[1])+']\n','white',1)

def prompt_str_not_in_options(name,arg,str_options):
    printf('<'+name+'>: '+'\''+arg+'\' is not in ['+','.join(str_options)+']\n','white',1)

def prompt_wrong_num_of_args(command,args_expected,args_given):
    printf('Command \''+command+'\' expects '+str(args_expected)+' argument'+('s' if args_expected!=1 else '')+', but '+str(args_given)+' '+('was' if args_given==1 else 'were')+' given\n','white',1)

def prompt_invalid_command(command):
    printf('\''+command+'\' does not name a command\n','white',1)

def prompt_updating_contest_gym_data_cf():
    printf('Updating cf contest+gym data\n','magenta',1)

def prompt_updating_contest_data_atc():
    printf('Updating atc contest data\n','magenta',1)

def prompt_io(test_idx,test_in,test_out):
    printf('[Test #'+str(test_idx)+']\n','white',1)
    printf('Input\n','blue',1)
    printf(test_in)
    printf('Output\n','blue',1)
    printf(test_out)

def prompt_help(help_tp):
    printf(commands.commands_zero,'blue',1)
    help=''
    if(help_tp==strings.help_contest):
        help+=commands.commands_contest
    elif(help_tp==strings.help_problem):
        help+=commands.help_string
    arg=0
    comm=1
    for c in help:
        if(c=='<'): arg=1
        if(c=='|'): comm=0
        if(arg==1):
            printf(c,'white',1)
        elif(comm==1):
            printf(c,('cyan' if help_tp==strings.help_problem else 'yellow'),(1 if help_tp==strings.help_problem else 0))
        elif(comm==0):
            printf(c,'white')
        if(c=='>'): arg=0
        if(c=='\n'): comm=1
