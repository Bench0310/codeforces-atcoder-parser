import output_setup
import prompt_handling
import website_handler
from contest_class import Contest
import file_management
import strings
import system_action
output_setup.init()

path=['C','Bench','CodeHub','Test']
user='Bench'

while(True):
    prompt_handling.prompt_user(user)
    contest_id=input()
    if(contest_id=='update'):
        website_handler.get_contest_url(path,'-1')
    elif(contest_id=='cls'):
        system_action.clear_screen()
    elif(contest_id=='help'):
        prompt_handling.prompt_help(strings.help_contest)
    elif(contest_id=='exit'):
        break
    elif(contest_id.isdigit()):
        url=website_handler.get_contest_url(path,contest_id)
        if(url!=''):
            contest=Contest(path,contest_id,url)
            while(True):
                prompt_handling.prompt_user_contest(user,contest_id)
                if(contest.solve()==0):
                    break
                prompt_handling.prompt_newline(1)
        else:
            prompt_handling.prompt_contest_not_found()
    else:
        prompt_handling.prompt_invalid_command(contest_id)
    prompt_handling.prompt_newline(1)
