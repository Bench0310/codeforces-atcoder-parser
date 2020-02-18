import os

def file_exists(path):
    return os.path.exists(path)

def create_folder(path):
    os.mkdir(path)

def create_file_win(path,content):
    f=open(path,'w')
    f.write(content)
    f.close()

def create_file_wsl(path,content):
    f=open(path,'w',newline='\n')
    f.write(content)
    f.close()

def read_file(path):
    f=open(path,'r')
    temp=f.read()
    f.close()
    return temp
