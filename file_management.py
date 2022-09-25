import os
import string_manip
import glob

def file_exists(path):
    return os.path.exists(string_manip.path_win(path))

def create_folder(path):
    os.mkdir(string_manip.path_win(path))

def create_file_win(path,content):
    f=open(string_manip.path_win(path),'w')
    f.write(content)
    f.close()

def create_file_wsl(path,content):
    f=open(string_manip.path_win(path),'w',newline='\n')
    f.write(content)
    f.close()

def read_file(path):
    f=open(string_manip.path_win(path),'r',encoding='utf8')
    temp=f.read()
    f.close()
    return temp

def delete_file(path):
    if(file_exists(path)):
        os.remove(string_manip.path_win(path))

def delete_empty_folder(path):
    if(file_exists(path)):
        os.rmdir(string_manip.path_win(path))

def list_files(path,extension=''):
    return [os.path.basename(t)[:len(os.path.basename(t))-len(extension)] for t in glob.glob(string_manip.path_win(path+['*'+extension]))]
