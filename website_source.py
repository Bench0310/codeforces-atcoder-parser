import requests
import strings

contest_list_source=None
contest_data_source=None

def get_source(url):
    r=requests.get(url)
    while(not r):
        print(strings.message_not_responding)
        r=requests.get(url)
    return r.text

def get_contest_list():
    global contest_list_source
    if(contest_list_source==None):
        contest_list_source=get_source(strings.url_contest_list)
    return contest_list_source

def get_contest_data(contest_id):
    global contest_data_source
    if(contest_data_source==None):
        contest_data_source=get_source(strings.url_contest_left+str(contest_id)+strings.url_contest_right)
    return contest_data_source
