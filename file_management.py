"""Provides functions for managing files."""

import os
import glob
import string_manip

def file_exists(path):
    return os.path.exists(string_manip.path_win(path))

def create_folder(path):
    os.mkdir(string_manip.path_win(path))

def create_file_win(path, content):
    with open(string_manip.path_win(path), 'w', encoding='utf8') as f:
        f.write(content)

def create_file_wsl(path, content):
    with open(string_manip.path_win(path), 'w', encoding='utf8', newline='\n') as f:
        f.write(content)

def read_file(path):
    with open(string_manip.path_win(path), 'r', encoding='utf8') as f:
        temp = f.read()
    return temp

def delete_file(path):
    if file_exists(path):
        os.remove(string_manip.path_win(path))

def delete_empty_folder(path):
    if file_exists(path):
        os.rmdir(string_manip.path_win(path))

def list_files(path, extension=''):
    return [os.path.basename(t)[:len(os.path.basename(t))-len(extension)] for t in glob.glob(string_manip.path_win(path+['*'+extension]))]
