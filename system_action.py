import subprocess
import os

def run_bash(path,args):
    command='wsl '+path
    for arg in args:
        command+=' '+str(arg)
    subprocess.run(command,shell=False)

def open_file(path):
    os.startfile(path)

def clear_screen():
    os.system('cls')

def copy_to_clipboard(content):
    os.system('@echo '+content+' | clip')
