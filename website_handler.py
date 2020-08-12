import requests
import prompt_handling
import file_management
import strings
import string_manip

def get_source(url,platform):
    r=requests.get(url)
    while(r.status_code>=500):
        prompt_handling.prompt_platform_not_responding(platform)
        r=requests.get(url)
    return r.text

def get_contest_url_cf(path,contest_id):
    contest_data=(file_management.read_file(path+['contest_data.txt']) if file_management.file_exists(path+['contest_data.txt']) else '')
    gym_data=(file_management.read_file(path+['gym_data.txt']) if file_management.file_exists(path+['gym_data.txt']) else '')
    url=''
    if(contest_data.find('> '+contest_id+'\n')!=-1):
        url='https://codeforces.com/contest/'+contest_id+'/problems'
    elif(gym_data.find('> '+contest_id+'\n')!=-1):
        url='https://codeforces.com/gym/'+contest_id+'/problems'
    else:
        prompt_handling.prompt_updating_contest_gym_data_cf()
        contest_data_source=get_source('https://codeforces.com/api/contest.list',strings.pl_cf)
        contest_data=''
        source_index_left=contest_data_source.find('"id":')
        while(source_index_left!=-1):
            source_index_right=contest_data_source.find(',',source_index_left)
            contest_data+='> '+contest_data_source[source_index_left+len('"id":'):source_index_right]+'\n'
            source_index_left=contest_data_source.find('"id":',source_index_left+1)
        gym_data_source=get_source('https://codeforces.com/api/contest.list?gym=true',strings.pl_cf)
        gym_data=''
        source_index_left=gym_data_source.find('"id":')
        while(source_index_left!=-1):
            source_index_right=gym_data_source.find(',',source_index_left)
            gym_data+='> '+gym_data_source[source_index_left+len('"id":'):source_index_right]+'\n'
            source_index_left=gym_data_source.find('"id":',source_index_left+1)
        file_management.create_file_win(path+['contest_data.txt'],contest_data)
        file_management.create_file_win(path+['gym_data.txt'],gym_data)
        if(contest_data.find('> '+contest_id+'\n')!=-1):
            url='https://codeforces.com/contest/'+contest_id+'/problems'
        elif(gym_data.find('> '+contest_id+'\n')!=-1):
            url='https://codeforces.com/gym/'+contest_id+'/problems'
    return url

def get_contest_url_atc(path,contest_id):
    contest_data=(file_management.read_file(path+['contest_data.txt']) if file_management.file_exists(path+['contest_data.txt']) else '')
    url=''
    if(contest_data.find('> '+contest_id.lower()+'\n')!=-1):
        url='https://atcoder.jp/contests/'+contest_id.lower()+'/tasks_print'
    else:
        prompt_handling.prompt_updating_contest_data_atc()
        contest_data_source=get_source('https://atcoder.jp/contests/',strings.pl_atc)
        contest_data=''
        contest_data_right=contest_data_source.find('Recent Contests')
        source_index=contest_data_source.find('<td >')
        while(source_index!=-1 and source_index<contest_data_right):
            source_index_left=contest_data_source.find('/contests/',source_index)
            source_index_right=contest_data_source.find('"',source_index_left)
            contest_data+='> '+contest_data_source[source_index_left+len('/contests/'):source_index_right]+'\n'
            source_index=contest_data_source.find('<td >',source_index+1)
        page=1
        while(True):
            contest_data_source=get_source('https://atcoder.jp/contests/archive?page='+str(page),strings.pl_atc)
            source_index=contest_data_source.find('<td >')
            if(source_index==-1):
                break
            while(source_index!=-1):
                source_index_left=contest_data_source.find('/contests/',source_index)
                source_index_right=contest_data_source.find('"',source_index_left)
                contest_data+='> '+contest_data_source[source_index_left+len('/contests/'):source_index_right]+'\n'
                source_index=contest_data_source.find('<td >',source_index+1)
            page+=1
        file_management.create_file_win(path+['contest_data.txt'],contest_data)
        if(contest_data.find('> '+contest_id.lower()+'\n')!=-1):
            url='https://atcoder.jp/contests/'+contest_id.lower()+'/tasks_print'
    return url
