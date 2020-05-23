import subprocess
import os
import pyperclip

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
    pyperclip.copy(content)
