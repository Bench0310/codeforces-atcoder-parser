import subprocess
import os
import pyperclip
import string_manip

def run_bash(path,args):
    command='wsl '+string_manip.path_wsl_q(path)
    for arg in args:
        command+=' '+string_manip.quotify(str(arg))
    subprocess.run(command,shell=False)

def open_file(path):
    os.startfile(string_manip.path_win(path))

def run_command(command):
    os.system(command)

def copy_to_clipboard(content):
    pyperclip.copy(content)
