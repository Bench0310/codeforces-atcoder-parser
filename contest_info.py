from imports import *

def contest_exists(contest_id):
    contest_list_source=website_source.get_contest_list()
    return (contest_list_source.text.find('"id":'+str(contest_id))!=-1)

def get_problems():
    m=5
