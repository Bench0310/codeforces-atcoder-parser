def quotify(s):
    return '"'+s+'"'

def digit_pad(num,k):
    return f'{num:0{k}d}'

def path_win(path):
    res=path[0]+':'
    for cd in path[1:]: res+='\\'+cd
    return res

def path_wsl(path):
    res='/mnt/'+path[0].lower()
    for cd in path[1:]: res+='/'+cd
    return res

def path_wsl_exe(path):
    res='/mnt/'+path[0].lower()
    for cd in path[1:-1]: res+='/'+cd
    res+='/./'+path[-1]
    return res
