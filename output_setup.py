import colorama

def init():
    colorama.init()

colors={
    'black':'\033[30m',
    'red':'\033[31m',
    'green':'\033[32m',
    'yellow':'\033[33m',
    'blue':'\033[34m',
    'magenta':'\033[35m',
    'cyan':'\033[36m',
    'white':'\033[37m',
    'bold':'\033[1m',
    'end':'\033[0m'
}

def printf(message,color='white',bold=0):
    if(not color in colors): raise Exception(f'{color} does not name a color')
    print(colors['end']+colors[color]+(colors['bold'] if bold else '')+message+colors['end'],end='')

def set_color(color='white',bold=0):
    if(not color in colors): raise Exception(f'{color} does not name a color')
    print(colors['end']+colors[color]+(colors['bold'] if bold else ''),end='')
