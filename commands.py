from command_argument_class import Command,ArgumentInt,ArgumentStr
import strings

help_width=22
help_string_contest=''
help_string_problem=''
help_string_zero=''

argc_id=ArgumentStr('id',None,None)
argc_pl=ArgumentStr('pl',strings.pls,None)

argp_id=ArgumentStr('id',[],None)
argp_tp=ArgumentStr('tp',strings.tps,None)
argp_tl=ArgumentInt('tl',[1,60])
argp_num=ArgumentInt('num',[])
argp_cnt=ArgumentInt('cnt',[1,10000])

comms_contest=[]
commands_contest={}
comms_problem=[]
commands_problem={}

help_string_zero='Command'+' '*(help_width-len('Command'))+'| Description\n'

comms_contest=[
    Command('parse',[argc_id],'Parse contest <id>'),
    Command('offline',[argc_id],'Parse contest <id> from local txt file'),
    Command('update',[],'Update cf+atc contest data'),
    Command('updatex',[argc_pl],'Update <pl>={cf,atc} contest data'),
    Command('cls',[],'Clear screen'),
    Command('help',[],'Print this guide'),
    Command('exit',[],'Exit parser')
]

comms_problem=[
    Command('run',[argp_id],'Run <id> on current tests'),
    Command('code',[argp_id,argp_tp],'Open .cpp of <tp>={main,bf,ch,gen} of <id>'),
    Command('codeall',[],'Open .cpp of main of all problems'),
    Command('io',[argp_id],'Print all input and output tests of <id>'),
    Command('add',[argp_id],'Add test to <id>'),
    Command('keep',[argp_id,argp_num],'Keep first <num> tests of <id> and delete the rest'),
    Command('tl',[argp_id,argp_tl],'Set TL of <id> to <tl>'),
    Command('stress',[argp_id,argp_cnt],'Stress <id> on <cnt> tests'),
    Command('check',[argp_id,argp_cnt],'Check <id> on <cnt> tests'),
    Command('runv',[argp_id],'Run <id> on current tests, and only get verdicts'),
    Command('path',[argp_id],'Copy path of <id> to clipboard'),
    Command('yank',[argp_id],'Copy code of <id> to clipboard'),
    Command('dbg',[argp_id,argp_tp],'Open <tp>={main,bf,ch,gen} of <id> in gdb'),
    Command('cls',[],'Clear screen'),
    Command('help',[],'Print this guide'),
    Command('exit',[],'Exit contest')
]

for command in comms_contest:
    commands_contest[command.name]=command

for command in comms_problem:
    commands_problem[command.name]=command

def build_help_string(comms,optional_comms):
    help_string=''
    for command in comms:
        help=''
        if(command.name in optional_comms):
            help+='['+command.name+']'
        else:
            help+=command.name
        for argument in command.arguments:
            help+=' <'+argument.name+'>'
        help+=' '*(help_width-len(help))
        help+='| '+command.description
        help_string+=help+'\n'
    return help_string

help_string_contest=build_help_string(comms_contest,['parse'])
help_string_problem=build_help_string(comms_problem,['run'])
