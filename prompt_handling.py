from output_setup import printf,set_color
import commands
import strings

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
    printf('Contest not found!\n','red')

def prompt_codeforces_not_responding():
    printf('Codeforces not responding, retrying now!\n','red')

def prompt_wrong_num_of_args(command,args_expected,args_given):
    printf('Command \''+command+'\' expects '+str(args_expected)+' argument'+('s' if args_expected!=1 else '')+', but '+str(args_given)+' '+('was' if args_given==1 else 'were')+' given\n','white',1)

def prompt_invalid_command(command):
    printf('\''+command+'\' does not name a command\n','white',1)

def prompt_invalid_arg(arg,required_arg):
    printf('\''+arg+'\' does not name a <'+required_arg+'>\n','white',1)

def prompt_updating_contest_gym_data():
    printf('Updating contest+gym data\n','magenta',1)

def prompt_io(test_idx,test_in,test_out):
    printf('[Test #'+str(test_idx)+']\n','white',1)
    printf('Input\n','blue',1)
    printf(test_in)
    printf('Output\n','blue',1)
    printf(test_out)

def prompt_help(help_tp):
    printf(commands.commands_ini,'blue',1)
    help=''
    if(help_tp==strings.help_contest):
        help=commands.commands_contest
    elif(help_tp==strings.help_problem):
        help=commands.commands_problem
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
