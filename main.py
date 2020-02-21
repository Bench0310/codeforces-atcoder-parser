import output_setup
import prompt_handling
import website_handler
from contest_class import Contest
output_setup.init()

path=['C','Bench','CodeHub','Test']
user='Bench'
while(True):
    prompt_handling.prompt_user(user)
    contest_id=input()
    if(contest_id=='exit'):
        break
    url=''
    contests=website_handler.get_source('https://codeforces.com/api/contest.list')
    if(contests.find('"id":'+contest_id+',')!=-1):
        url='https://codeforces.com/contest/'+contest_id+'/problems'
    contests=website_handler.get_source('https://codeforces.com/api/contest.list?gym=true')
    if(contests.find('"id":'+contest_id+',')!=-1):
        url='https://codeforces.com/gym/'+contest_id+'/problems'
    if(url!=''):
        contest=Contest(path,contest_id,url)
        while(True):
            prompt_handling.prompt_user_contest(user,contest_id)
            if(contest.solve()==0):
                break
    else:
        prompt_handling.prompt_contest_not_found()
    prompt_handling.prompt_newline(3)
