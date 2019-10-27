import requests

contest_list_source=None
contest_data_source=None

def get_source(url):
    r=requests.get(url)
    while(not r):
        print('Codeforces not responding, retrying now!')
        r=requests.get(url)
    return r.text

def get_contest_list():
    global contest_list_source
    if(contest_list_source==None):
        contest_list_source=get_source('https://codeforces.com/api/contest.list')
    return contest_list_source

def get_contest_data(contest_id):
    global contest_data_source
    if(contest_data_source==None):
        contest_data_source=get_source(f'https://codeforces.com/contest/{contest_id}/problems')
    return contest_data_source
