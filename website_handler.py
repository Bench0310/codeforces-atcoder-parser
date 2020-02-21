import requests
import prompt_handling
import file_management
import string_manip

def get_source(url):
    r=requests.get(url)
    while(not r):
        prompt_handling.prompt_codeforces_not_responding()
        r=requests.get(url)
    return r.text

def get_contest_url(path,contest_id):
    contest_data=(file_management.read_file(string_manip.path_win(path+['contest_data.txt'])) if file_management.file_exists(string_manip.path_win(path+['contest_data.txt'])) else '')
    gym_data=(file_management.read_file(string_manip.path_win(path+['gym_data.txt'])) if file_management.file_exists(string_manip.path_win(path+['gym_data.txt'])) else '')
    url=''
    if(contest_data.find('> '+contest_id+'\n')!=-1):
        url='https://codeforces.com/contest/'+contest_id+'/problems'
    elif(gym_data.find('> '+contest_id+'\n')!=-1):
        url='https://codeforces.com/gym/'+contest_id+'/problems'
    else:
        prompt_handling.prompt_updating_contest_gym_data()
        contest_data_source=get_source('https://codeforces.com/api/contest.list')
        contest_data=''
        source_index_left=contest_data_source.find('"id":')
        while(source_index_left!=-1):
            source_index_right=contest_data_source.find(',',source_index_left)
            contest_data+='> '+contest_data_source[source_index_left+len('"id":'):source_index_right]+'\n'
            source_index_left=contest_data_source.find('"id":',source_index_left+1)
        gym_data_source=get_source('https://codeforces.com/api/contest.list?gym=true')
        gym_data=''
        source_index_left=gym_data_source.find('"id":')
        while(source_index_left!=-1):
            source_index_right=gym_data_source.find(',',source_index_left)
            gym_data+='> '+gym_data_source[source_index_left+len('"id":'):source_index_right]+'\n'
            source_index_left=gym_data_source.find('"id":',source_index_left+1)
        file_management.create_file_win(string_manip.path_win(path+['contest_data.txt']),contest_data)
        file_management.create_file_win(string_manip.path_win(path+['gym_data.txt']),gym_data)
        if(contest_data.find('> '+contest_id+'\n')!=-1):
            url='https://codeforces.com/contest/'+contest_id+'/problems'
        elif(gym_data.find('> '+contest_id+'\n')!=-1):
            url='https://codeforces.com/gym/'+contest_id+'/problems'
    return url
