import prompt_handling
import website_handler
from contest_class import Contest
import file_management
import strings
import system_action
import string_manip
import commands
prompt_handling.init()

user='Bench'
path_cf=['C','Bench','CodeHub','Codeforces']
path_atc=['C','Bench','CodeHub','AtCoder']

while(True):
    prompt_handling.prompt_user(user)
    contest_id=input()
    if(contest_id=='update'):
        website_handler.get_contest_url_cf(path_cf,'-1')
        website_handler.get_contest_url_atc(path_atc,'-1')
    elif(contest_id=='cls'):
        system_action.clear_screen()
    elif(contest_id=='help'):
        prompt_handling.prompt_help(strings.help_contest)
    elif(contest_id=='exit'):
        break
    elif(not ' ' in contest_id):
        contest_id=contest_id.upper()
        platform=('cf' if contest_id.isdigit() else 'atc')
        path_now=(path_cf if platform=='cf' else path_atc)
        if(platform=='cf'):
            url=website_handler.get_contest_url_cf(path_cf,contest_id)
        elif(platform=='atc'):
            url=website_handler.get_contest_url_atc(path_atc,contest_id)
        if(url!=''):
            contest=Contest(path_now,contest_id,url,platform)
            if(file_management.file_exists(path_now+[contest_id])==True):
                commands.arg_id.str_options=list(contest.problems)
                commands.ini()
                while(True):
                    prompt_handling.prompt_user_contest(user,contest_id)
                    if(contest.solve()==0):
                        break
                    prompt_handling.prompt_newline(1)
            else:
                prompt_handling.prompt_contest_no_problems()
        else:
            prompt_handling.prompt_contest_not_found()
    else:
        prompt_handling.prompt_invalid_command(contest_id)
    prompt_handling.prompt_newline(1)
