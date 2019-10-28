from output_setup import printf
import strings

def prompt_contest_id():
    print(strings.message_enter_contest_number)
    return int(input())

def prompt_contest_does_not_exist():
    print(strings.message_contest_does_not_exist)
    exit()
