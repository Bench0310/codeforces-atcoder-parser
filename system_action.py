import subprocess
import os

def run_batch(path):
    subprocess.call(path)

def clear_screen():
    os.system('cls')

def copy_to_clipboard(content):
    os.system('@echo '+content+' | clip')
