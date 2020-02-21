import requests
import prompt_handling

def get_source(url):
    r=requests.get(url)
    while(not r):
        prompt_handling.prompt_codeforces_not_responding()
        r=requests.get(url)
    return r.text
