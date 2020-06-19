import strings

def quotify(s):
    return '"'+s+'"'

def path_win(path):
    res=path[0]+':'
    for cd in path[1:]: res+='\\'+cd
    return res

def path_wsl(path):
    res='/mnt/'+path[0].lower()
    for cd in path[1:]: res+='/'+cd
    return res

def path_win_q(path):
    return quotify(path_win(path))

def path_wsl_q(path):
    return quotify(path_wsl(path))

def beautify_test(s):
    s=s.replace(strings.test_newline,'\n')
    s=s.replace(strings.test_smaller_than,'<')
    s=s.replace(strings.test_greater_than,'>')
    s=s.replace(strings.test_ampersand,'&')
    while(len(s)>0 and s[0]=='\n'):
        s=s[1:]
    while(len(s)>0 and s[-1]=='\n'):
        s=s[:-1]
    if(len(s)==0 or s[-1]!='\n'):
        s+='\n'
    return s

def code_wsl(s):
    s=s.replace('%I64d','%lld')
    return s
