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
