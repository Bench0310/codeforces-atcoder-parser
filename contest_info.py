from imports import *

def contest_exists(id):
    contest_list=requests.get('https://codeforces.com/api/contest.list')
    return (contest_list.text.find('"id":'+str(id))!=-1)
