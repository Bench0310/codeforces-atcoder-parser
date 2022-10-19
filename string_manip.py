"""Provides functions for string manipulations."""

import strings

def quotify(s):
    """Quotifies the given string."""
    return '"'+s+'"'

def path_win(path):
    """Creates the full Windows path."""
    res = path[0]+':'
    for nxt in path[1:]: res += '\\'+nxt
    return res

def path_wsl(path):
    """Creates the full WSL path."""
    res = '/mnt/'+path[0].lower()
    for nxt in path[1:]: res += '/'+nxt
    return res

def path_win_q(path):
    """Creates a quotified full Windows path."""
    return quotify(path_win(path))

def path_wsl_q(path):
    """Creates a quotified full WSL path."""
    return quotify(path_wsl(path))

def normalize_test(s):
    """Fix the testcase fetched from raw html."""
    s = s.replace(strings.test_newline, '\n')
    s = s.replace(strings.test_smaller_than, '<')
    s = s.replace(strings.test_greater_than, '>')
    s = s.replace(strings.test_ampersand, '&')
    return s

def beautify_test(s):
    """Fix the newlines at the start and end of the testcase."""
    while len(s) > 0 and s[0] == '\n':
        s = s[1:]
    while len(s) > 0 and s[-1] == '\n':
        s = s[:-1]
    s += '\n'
    return s
