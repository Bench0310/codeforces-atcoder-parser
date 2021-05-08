import colorama
from datetime import datetime
import commands
import strings

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

def get_input():
    return list(filter(None,input().lower().split(' ')))

def parse_input_level_contest():
    args=get_input()
    if(len(args)==0):
        args.append('')
    if(args[0]!='' and (not args[0] in commands.commands_contest)):
        args=['parse']+args
    command=args[0]
    if(not command in commands.commands_contest):
        prompt_invalid_command(command)
        return ['',{},False]
    if(commands.commands_contest[command].parse(args[1:])==False):
        return ['',{},False]
    arg={}
    arg_now=1
    for argument in commands.commands_contest[command].arguments:
        arg[argument.name]=args[arg_now]
        arg_now+=1
    return [command,arg,True]

def parse_input_level_problem_prepare(active_problem_index):
    args=get_input()
    prompt_time()
    if(len(args)==0):
        args.append('')
    if(len(args)==1 and args[0] in commands.argp_id.options):
        args=['run']+args
    command=args[0]
    if(not command in commands.commands_problem):
        prompt_invalid_command(command)
        return [[],False,-1]
    arguments=commands.commands_problem[command].arguments
    arg_id_pos=-1
    for i,argument in enumerate(arguments):
        if(argument.name=='id'):
            if(len(args)-1==len(arguments)-1):
                args.insert(i+1,active_problem_index)
            arg_id_pos=i+1
    return [args,True,arg_id_pos]

def parse_input_level_problem(args):
    command=args[0]
    if(commands.commands_problem[command].parse(args[1:])==False):
        return ['',{},False]
    arg={}
    arg_now=1
    for argument in commands.commands_problem[command].arguments:
        arg[argument.name]=args[arg_now]
        arg_now+=1
    return [command,arg,True]

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

def prompt_time():
    printf('['+datetime.now().strftime('%H:%M:%S')+']\n')

def prompt_offline_command():
    printf('Link copied, press enter to continue','magenta',1)

def prompt_contest_not_found():
    printf('Contest not found\n','red')

def prompt_contest_no_problems():
    printf('Contest has no problems\n','red')

def prompt_platform_not_responding(platform):
    printf(('Codeforces' if platform==strings.pl_cf else 'AtCoder')+' not responding, retrying now\n','red')

def prompt_not_an_int(name,arg):
    printf('<'+name+'>: '+'\''+arg+'\' is not an int\n','white',1)

def prompt_int_not_in_range(name,arg,opt_range):
    printf('<'+name+'>: '+'\''+arg+'\' is not in range ['+str(opt_range[0])+','+str(opt_range[1])+']\n','white',1)

def prompt_str_not_in_options(name,arg,options):
    printf('<'+name+'>: '+'\''+arg+'\' is not in [\''+'\',\''.join(options)+'\']\n','white',1)

def prompt_str_in_forbidden(name,arg):
    printf('<'+name+'>: '+'\''+arg+'\' is forbidden\n','white',1)

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
    if(len(test_in)==0 or test_in[-1]!='\n'): printf('\n')
    printf('Output\n','blue',1)
    printf(test_out)
    if(len(test_out)==0 or test_out[-1]!='\n'): printf('\n')

def prompt_help(level):
    printf(commands.help_string_zero,'blue',1)
    help=commands.help_string_contest if level==strings.level_contest else commands.help_string_problem if level==strings.level_problem else ''
    arg=0
    comm=1
    for c in help:
        if(c=='<'): arg=1
        if(c=='|'): comm=0
        if(arg==1):
            printf(c,'white',1)
        elif(comm==1):
            printf(c,('cyan' if level==strings.level_problem else 'yellow'),(1 if level==strings.level_problem else 0))
        elif(comm==0):
            printf(c,'white')
        if(c=='>'): arg=0
        if(c=='\n'): comm=1
