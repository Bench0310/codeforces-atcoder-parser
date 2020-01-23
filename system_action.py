import subprocess
import os

def run_batch(path):
    subprocess.call(path,timeout=5)

def run_batch_timeout(path,process_name,tl=2):
    try:
        subprocess.call(path,timeout=tl)
        return 1
    except subprocess.TimeoutExpired:
        os.system('taskkill /im '+process_name+' /f >nul 2>&1')
        return 0

def clear_screen():
    os.system('cls')

def copy_to_clipboard(content):
    os.system('@echo '+content+' | clip')
