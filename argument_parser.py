import strings
import prompt_handling

def parse_tp(tp):
    if(tp in strings.tps):
        return 1
    else:
        prompt_handling.prompt_invalid_arg(tp,'tp')
        return 0

def parse_id(id,ids):
    if(id in ids):
        return 1
    else:
        prompt_handling.prompt_invalid_arg(id,'id')
        return 0

def parse_num(num):
    if(num.isdigit()):
        return 1
    else:
        prompt_handling.prompt_invalid_arg(num,'num')

def parse_tl(tl):
    if(tl.isdigit()):
        return 1
    else:
        prompt_handling.prompt_invalid_arg(tl,'tl')
