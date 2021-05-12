import prompt_handling
import website_handler
from contest_class import Contest
import file_management
from file_management import Navigator
import strings
import system_action
import string_manip
import commands

user='Bench'
path=['C','Bench','CodeHub']
path_cf=['C','Bench','CodeHub','Codeforces']
path_atc=['C','Bench','CodeHub','AtCoder']
path_offline=['C','Users','Benja','Downloads','__contest__.txt']

Navigator.default=path
navigator=Navigator()

while(True):
<<<<<<< Updated upstream
    prompt_handling.prompt_user(user)
=======
    prompt_handling.prompt_user(user,navigator.path[len(Navigator.default):])
>>>>>>> Stashed changes
    command,arg,success=prompt_handling.parse_input_level_contest()
    if(success==False):
        prompt_handling.prompt_newline(1)
        continue
    if(command=='parse' or command=='offline'):
        arg['id']=arg['id'].upper()
        platform=(strings.pl_cf if arg['id'].isdigit() else strings.pl_atc)
        path_now=(path_cf if platform==strings.pl_cf else path_atc)
        if(platform==strings.pl_cf):
            url=website_handler.get_contest_url_cf(path_cf,arg['id'])
        elif(platform==strings.pl_atc):
            url=website_handler.get_contest_url_atc(path_atc,arg['id'])
        if(url!=''):
            if(command=='offline' and file_management.file_exists(path_now+[arg['id']])==False):
                system_action.copy_to_clipboard(strings.chrome_view_source+url)
                prompt_handling.prompt_offline_command()
                file_management.create_file_win(path_offline,'')
                system_action.open_file(path_offline)
                input()
            contest=Contest(path_now+[arg['id']],arg['id'],url,platform,(None if command=='parse' else path_offline))
            if(file_management.file_exists(path_now+[arg['id']])==True):
<<<<<<< Updated upstream
=======
                navigator.path=Navigator.default.copy()
>>>>>>> Stashed changes
                commands.argp_id.options=list(contest.problems)
                while(True):
                    prompt_handling.prompt_user_contest(user,arg['id'],None)
                    if(contest.solve()==False):
                        break
                    prompt_handling.prompt_newline(1)
            else:
                prompt_handling.prompt_contest_no_problems()
        else:
            prompt_handling.prompt_contest_not_found()
    elif(command=='update'):
        website_handler.get_contest_url_cf(path_cf,'-1')
        website_handler.get_contest_url_atc(path_atc,'-1')
    elif(command=='updatex'):
        if(arg['pl']==strings.pl_cf):
            website_handler.get_contest_url_cf(path_cf,'-1')
        elif(arg['pl']==strings.pl_atc):
            website_handler.get_contest_url_atc(path_atc,'-1')
    elif(command=='cd'):
        if(navigator.cd(arg['path'])==False):
            prompt_handling.prompt_invalid_path()
        if(file_management.folder_is_contest(navigator.path)):
            contest=Contest(navigator.path,'',None,None,None)
            commands.argp_id.options=list(contest.problems)
            while(True):
                prompt_handling.prompt_user_contest(user,None,navigator.path[len(Navigator.default):])
                if(contest.solve()==False):
                    break
                prompt_handling.prompt_newline(1)
            navigator.path.pop()
    elif(command=='cls'):
        system_action.clear_screen()
    elif(command=='help'):
        prompt_handling.prompt_help(strings.level_contest)
    elif(command=='exit'):
        break
    prompt_handling.prompt_newline(1)

prompt_handling.set_color()
