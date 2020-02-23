commands_ini=(
'Command               | Description\n')

commands_problem=(
'<id>                  | Run <id> on current tests\n'
'code <id> <tp>        | Open .cpp of <tp>={main,bf,ch,gen} of <id>\n'
'codeall               | Open .cpp of main of all problems\n'
'debug <id> <tp>       | Open .cbp of <tp>={main,bf,ch,gen} of <id>\n'
'debugall              | Open .cbp of main of all problems\n'
'io <id>               | Print all input and output tests of <id>\n'
'add <id>              | Add test to <id>\n'
'keep <id> <num>       | Keep first <num> tests of <id> and delete the rest\n'
'rm <id> <num>         | Delete last <num> tests of <id>\n'
'tl <id> <tl>          | Set TL of <id> to <tl>\n'
'stress <id> <num>     | Stress <id> on <num> tests\n'
'check <id> <num>      | Check <id> on <num> tests\n'
'path                  | Copy path of last used <id> to clipboard\n'
'pathx <id>            | Copy path of <id> to clipboard\n'
'cls                   | Clear screen\n'
'help                  | Print this guide\n'
'exit                  | Exit contest\n')

commands_contest=(
'<contest_id>          | Parse contest <contest_id>\n'
'update                | Update contest+gym data\n'
'cls                   | Clear screen\n'
'help                  | Print this guide\n'
'exit                  | Exit parser\n')
