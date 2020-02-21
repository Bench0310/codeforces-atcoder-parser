from output_setup import printf,set_color

def prompt_newline(num):
    for i in range(num):
        print('')

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
    printf('Command \''+command+'\' is not a command\n','white',1)

def prompt_invalid_arg(arg,required_arg):
    printf('\''+arg+'\' does not name a <'+required_arg+'>\n','white',1)

def prompt_help():
    printf('This should print the help guide\n','white',1)
