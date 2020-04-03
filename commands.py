from command_argument_class import Command,Argument
import strings

help_width=22
help_string=''

arg_id=Argument('id',strings.ctp_str,0,[])
arg_tp=Argument('tp',strings.ctp_str,0,strings.tps)
arg_tl=Argument('tl',strings.ctp_num,[1,60],0)
arg_num=Argument('num',strings.ctp_num,[0,10000],0)
arg_cnt=Argument('cnt',strings.ctp_num,[1,10000],0)

commands_zero='Command'+' '*(help_width-len('Command'))+'| Description\n'
commands=[]

def ini():
    global commands
    global help_string
    commands=[
        Command('code',[arg_id,arg_tp],'Open .cpp of <tp>={main,bf,ch,gen} of <id>'),
        Command('codeall',[],'Open .cpp of main of all problems'),
        Command('debug',[arg_id,arg_tp],'Open .cbp of <tp>={main,bf,ch,gen} of <id>'),
        Command('debugall',[],'Open .cbp of main of all problems'),
        Command('io',[arg_id],'Print all input and output tests of <id>'),
        Command('add',[arg_id],'Add test to <id>'),
        Command('keep',[arg_id,arg_num],'Keep first <num> tests of <id> and delete the rest'),
        Command('rm',[arg_id,arg_num],'Delete last <num> tests of <id>'),
        Command('tl',[arg_id,arg_tl],'Set TL of <id> to <tl>'),
        Command('stress',[arg_id,arg_cnt],'Stress <id> on <cnt> tests'),
        Command('check',[arg_id,arg_cnt],'Check <id> on <cnt> tests'),
        Command('path',[],'Copy path of last used <id> to clipboard'),
        Command('pathx',[arg_id],'Copy path of <id> to clipboard'),
        Command('cls',[],'Clear screen'),
        Command('help',[],'Print this guide'),
        Command('exit',[],'Exit contest')
    ]
    help_string=''
    for command in commands:
        help=''
        help+=command.name
        for argument in command.arguments:
            help+=' <'+argument.name+'>'
        help+=' '*(help_width-len(help))
        help+='| '+command.description
        help_string+=help+'\n'

commands_contest=(
'<contest_id>          | Parse contest <contest_id>\n'
'update                | Update contest+gym data\n'
'cls                   | Clear screen\n'
'help                  | Print this guide\n'
'exit                  | Exit parser\n')
