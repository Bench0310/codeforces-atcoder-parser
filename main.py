import output_setup
import prompt_handling
import website_handler
from contest_class import Contest
import file_management
import strings
import system_action
import string_manip
import commands
output_setup.init()

path_cf=['C','Bench','CodeHub','Codeforces']
path_atc=['C','Bench','CodeHub','AtCoder']
user='Bench'

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
    elif(contest_id.isdigit()):
        url=website_handler.get_contest_url_cf(path_cf,contest_id)
        if(url!=''):
            contest=Contest(path_cf,contest_id,url,'cf')
            if(file_management.file_exists(string_manip.path_win(path_cf+[contest_id]))==True):
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
    elif(not ' ' in contest_id):
        contest_id=contest_id.upper()
        url=website_handler.get_contest_url_atc(path_atc,contest_id)
        if(url!=''):
            contest=Contest(path_atc,contest_id,url,'atc')
            if(file_management.file_exists(string_manip.path_win(path_atc+[contest_id]))==True):
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
