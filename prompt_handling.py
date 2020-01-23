from output_setup import printf,set_color
import strings
import string_manip

def prompt_newline(num):
    for i in range(num):
        print('')

def prompt_contest_id():
    printf(strings.message_enter_contest_number)
    set_color('yellow')
    contest_id=int(input())
    set_color('white')
    return contest_id

def prompt_contest_does_not_exist():
    print(strings.message_contest_does_not_exist)
    exit()

def prompt_codeforces_not_responding():
    printf(strings.message_codeforces_not_responding+'\n','red')

def prompt_succesful_parsing():
    printf(strings.message_successful_parsing+'\n','green')

def prompt_already_parsed():
    printf(strings.message_already_parsed+'\n','magenta')

def prompt_optional_cbopener():
    printf(strings.message_optional_cbopener,'magenta',1)
    temp=input().upper()
    return (temp=='Y')

def prompt_problem_index_checker():
    printf(strings.message_problem_index)
    set_color('cyan',1)
    temp=input()
    set_color('white')
    return temp

def prompt_unrecognized_problem_index(problem_index_checker):
    print(problem_index_checker+strings.message_unrecognized_problem_index)

def prompt_test(sample_test):
    printf('[Test #'+string_manip.k_digit(sample_test,2)+'] ',bold=1)

def prompt_test_status(status):
    if(status=='OK'):
        printf('OK\n','green',1)
    elif(status=='TLE'):
        printf('TLE\n','yellow')
    elif(status=='WA'):
        printf('WA\n','red',1)

def prompt_output_comparison(sample_test_output,sample_test_answer):
    printf('Received:\n','blue',1)
    printf(sample_test_output)
    printf('Expected:\n','blue',1)
    printf(sample_test_answer)
