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
    if(len(s)>0):
        l=0
        while(l<len(s) and s[l]=='\n'):
            l+=1
        s=s[l:]
    if(len(s)==0 or s[-1]!='\n'):
        s+='\n'
    return s

def code_wsl(s):
    s=s.replace('%I64d','%lld')
    return s

def code_win(s):
    s=s.replace('%lld','%I64d')
    return s
