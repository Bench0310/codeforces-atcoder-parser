import subprocess

def run_bash(path,args):
    command='wsl '+path
    for arg in args:
        command+=' '+str(arg)
    subprocess.run(command,shell=False)

def open_file(path):
    subprocess.run(path,shell=True)

def clear_screen():
    subprocess.run('cls',shell=True)

def copy_to_clipboard(content):
    subprocess.run('@echo '+content+' | clip',shell=True)
