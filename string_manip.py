import strings

def quotify(s):
    return '"'+s+'"'

def k_digit(num,k):
    return f'{num:0{k}d}'

def beautify_sample(s):
    s=s.replace(strings.sample_test_newline,'\n')
    s=s.replace(strings.sample_test_smaller_than,'<')
    s=s.replace(strings.sample_test_greater_than,'>')
    while(len(s) and s[0]=='\n'):
        s=s[1:]
    while(len(s) and s[-1]=='\n'):
        s=s[:-1]
    s+='\n'
    return s
