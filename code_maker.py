import path_maker
import string_manip
import name_maker

def code_cpp():
    temp=('#include <bits/stdc++.h>\n'
          '\n'
          'using namespace std;\n'
          '\n'
          'int main()\n'
          '{\n'
          '    \n'
          '    return 0;\n'
          '}\n')
    return temp

def code_cmd_compile(self,tp):
    temp='@echo off\n'
    temp+='cd '+string_manip.quotify(path_maker.path_checker(self))+'\n'
    temp+='g++ -std=c++17 -Wl,--stack,268435456 -Wall -Wextra -O3 -o '+string_manip.quotify(path_maker.path_checker_exe(self,tp))+' '+string_manip.quotify(path_maker.path_problem_cpp(self,tp))+'\n'
    return temp

def code_cmd_test(self,j):
    temp='@echo off\n'
    temp+=string_manip.quotify(path_maker.path_checker_exe(self,'main'))+' < '+string_manip.quotify(path_maker.path_io_in(self,j))+' > '+string_manip.quotify(path_maker.path_checker_output(self,j))+'\n'
    return temp

def code_cmd_bf(self):
    temp='@echo off\n'
    temp+=string_manip.quotify(path_maker.path_checker_exe(self,'bf'))+' < '+string_manip.quotify(path_maker.path_checker_stressin(self))+' > '+string_manip.quotify(path_maker.path_checker_stressout(self))+'\n'
    return temp

def code_cmd_gen(self):
    temp='@echo off\n'
    temp+=string_manip.quotify(path_maker.path_checker_exe(self,'gen'))+' > '+string_manip.quotify(path_maker.path_checker_stressin(self))+'\n'
    return temp

def code_cmd_stresstest(self):
    temp='@echo off\n'
    temp+=string_manip.quotify(path_maker.path_checker_exe(self,'main'))+' < '+string_manip.quotify(path_maker.path_checker_stressin(self))+' > '+string_manip.quotify(path_maker.path_checker_stressoutput(self))+'\n'
    return temp

def code_cbp(self,tp):
    temp=('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n'
          '<CodeBlocks_project_file>\n'
          '	<FileVersion major="1" minor="6" />\n'
          '	<Project>\n'
          '		<Option title="'+name_maker.name_problem_cbp(self,tp)+'" />\n'
          '		<Option pch_mode="2" />\n'
          '		<Option compiler="gcc" />\n'
          '		<Build>\n'
          '			<Target title="Debug">\n'
          '				<Option output="bin/Debug/'+name_maker.name_problem_cbp(self,tp)+'" prefix_auto="1" extension_auto="1" />\n'
          '				<Option object_output="obj/Debug/" />\n'
          '				<Option type="1" />\n'
          '				<Option compiler="gcc" />\n'
          '				<Compiler>\n'
          '					<Add option="-std=c++17" />\n'
          '					<Add option="-g" />\n'
          '				</Compiler>\n'
          '			</Target>\n'
          '			<Target title="Release">\n'
          '				<Option output="bin/Release/'+name_maker.name_problem_cbp(self,tp)+'" prefix_auto="1" extension_auto="1" />\n'
          '				<Option object_output="obj/Release/" />\n'
          '				<Option type="1" />\n'
          '				<Option compiler="gcc" />\n'
          '				<Compiler>\n'
          '					<Add option="-O2" />\n'
          '				</Compiler>\n'
          '				<Linker>\n'
          '					<Add option="-s" />\n'
          '				</Linker>\n'
          '			</Target>\n'
          '		</Build>\n'
          '		<Compiler>\n'
          '			<Add option="-Wall" />\n'
          '			<Add option="-fexceptions" />\n'
          '		</Compiler>\n'
          '		<Unit filename="'+name_maker.name_problem_cpp(self,tp)+'" />\n'
          '		<Extensions>\n'
          '			<code_completion />\n'
          '			<envvars />\n'
          '			<debugger />\n'
          '		</Extensions>\n'
          '	</Project>\n'
          '</CodeBlocks_project_file>\n')
    return temp

def code_problem_index(contest):
    temp=''
    for self in contest:
        temp+=self.contest_id+' '+self.problem_index+'\n'
    temp=temp[:-1]
    return temp

def code_problem_name(contest):
    temp=''
    for self in contest:
        temp+=self.problem_name+'\n'
    temp=temp[:-1]
    return temp

def code_cpp_opener(self,tp):
    temp='@echo off\n'
    temp+=string_manip.quotify(path_maker.path_problem_cpp(self,tp))+'\n'
    return temp

def code_cbp_opener(self,tp):
    temp='@echo off\n'
    temp+=string_manip.quotify(path_maker.path_problem_cbp(self,tp))+'\n'
    return temp
