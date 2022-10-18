"""Provides functions for string manipulations."""

import strings

def quotify(s):
    return '"'+s+'"'

def path_win(path):
    res = path[0]+':'
    for nxt in path[1:]: res += '\\'+nxt
    return res

def path_wsl(path):
    res = '/mnt/'+path[0].lower()
    for nxt in path[1:]: res += '/'+nxt
    return res

def path_win_q(path):
    return quotify(path_win(path))

def path_wsl_q(path):
    return quotify(path_wsl(path))

def normalize_test(s):
    s = s.replace(strings.test_newline, '\n')
    s = s.replace(strings.test_smaller_than, '<')
    s = s.replace(strings.test_greater_than, '>')
    s = s.replace(strings.test_ampersand, '&')
    return s

def beautify_test(s):
    while len(s) > 0 and s[0] == '\n':
        s = s[1:]
    while len(s) > 0 and s[-1] == '\n':
        s = s[:-1]
    s += '\n'
    return s
