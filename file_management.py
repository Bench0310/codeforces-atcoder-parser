import os
import string_manip

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

def folder_is_contest(path):
    return file_exists(path+['metadata.txt'])

class Navigator:
    default=[]
    def __init__(self):
        self.path=Navigator.default.copy()
    def move(self,folder):
        if(folder_is_contest(self.path)==True):
            return False
        if(folder=='' or folder.isspace()):
            return False
        elif(folder=='\\'):
            self.path=Navigator.default.copy()
        elif(folder=='..'):
            if(len(self.path)>len(Navigator.default)):
                self.path.pop()
        else:
            if(file_exists(self.path+[folder])):
                self.path.append(os.path.basename(os.path.realpath(string_manip.path_win(self.path+[folder]))))
            else:
                return False
        return True
    def cd(self,arg):
        arg=arg.replace('/','\\')
        folders=arg.split('\\')
        if(arg[0]=='\\'):
            folders=folders[1:]
        if(arg[-1]=='\\'):
            folders=folders[:-1]
        if(arg[0]=='\\'):
            folders.insert(0,'\\')
        old_path=self.path.copy()
        for folder in folders:
            if(self.move(folder)==False):
                self.path=old_path
                return False
        return True
