from command_argument_class import Command,ArgumentNum,ArgumentStr
import strings

argc_id=ArgumentStr('id',None)
argc_pl=ArgumentStr('pl',strings.pls)

argp_id=ArgumentStr('id',[])
argp_tp=ArgumentStr('tp',strings.tps)
argp_tl=ArgumentNum('tl',[1,10])
argp_num=ArgumentNum('num',[0,100000])
argp_cnt=ArgumentNum('cnt',[1,100000])
argp_rgtp=ArgumentStr('rgtp',[strings.tp_bf,strings.tp_ch])

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
    Command('debug',[argp_id,argp_tp],'Open .cbp of <tp>={main,bf,ch,gen} of <id>'),
    Command('debugall',[],'Open .cbp of main of all problems'),
    Command('io',[argp_id],'Print all input and output tests of <id>'),
    Command('add',[argp_id],'Add test to <id>'),
    Command('keep',[argp_id,argp_num],'Keep first <num> tests of <id> and delete the rest'),
    Command('rm',[argp_id,argp_num],'Delete last <num> tests of <id>'),
    Command('tl',[argp_id,argp_tl],'Set TL of <id> to <tl>'),
    Command('runbf',[argp_id],'Run bf of <id> on current tests'),
    Command('stress',[argp_id,argp_cnt],'Stress <id> on <cnt> tests'),
    Command('check',[argp_id,argp_cnt],'Check <id> on <cnt> tests'),
    Command('regen',[argp_id,argp_rgtp],'Rerun <rgtp>={bf,ch} of <id> on previous gen'),
    Command('path',[],'Copy path[cf]/code[atc] of last used <id> to clipboard'),
    Command('pathx',[argp_id],'Copy path[cf]/code[atc] of <id> to clipboard'),
    Command('dbg',[argp_id,argp_tp],'Open <tp>={main,bf,ch,gen} of <id> in gdb'),
    Command('cls',[],'Clear screen'),
    Command('help',[],'Print this guide'),
    Command('exit',[],'Exit contest')
]

commands_contest=dict(zip([command.name for command in comms_contest],comms_contest))
commands_problem=dict(zip([command.name for command in comms_problem],comms_problem))

help_width=22

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

help_string_zero='Command'+' '*(help_width-len('Command'))+'| Description\n'
help_string_contest=build_help_string(comms_contest,['parse'])
help_string_problem=build_help_string(comms_problem,['run'])
