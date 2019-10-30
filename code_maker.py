import contest_info
import path_maker
import string_manip

problem_index=contest_info.problem_index
problem_name=contest_info.problem_name
sample_test_in=contest_info.sample_test_in
sample_test_out=contest_info.sample_test_out

def code_main():
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

def code_cmd(contest_id,i):
    temp='@echo off\n'
    temp+='cd '+string_manip.quotify(path_maker.path_checker(contest_id))+'\n'
    temp+='g++ -std=c++11 -Wl,--stack,268435456 -Wall -Wextra -O3 -o '+string_manip.quotify(path_maker.path_checker_exe(contest_id,i))+' '+string_manip.quotify(path_maker.path_problem_main(contest_id,i))+'\n'
    for j in range(len(sample_test_in[i])):
          temp+=string_manip.quotify(path_maker.path_checker_exe(contest_id,i))+' < '+string_manip.quotify(path_maker.path_io_in(contest_id,i,j+1))+' > '+string_manip.quotify(path_maker.path_checker_output(contest_id,i,j+1))+'\n'
    return temp

def code_cbp(contest_id,i):
    temp=('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n'
          '<CodeBlocks_project_file>\n'
          '	<FileVersion major="1" minor="6" />\n'
          '	<Project>\n'
          '		<Option title="'+str(contest_id)+problem_index[i]+' '+problem_name[i]+'" />\n'
          '		<Option pch_mode="2" />\n'
          '		<Option compiler="gcc" />\n'
          '		<Build>\n'
          '			<Target title="Debug">\n'
          '				<Option output="bin/Debug/'+str(contest_id)+problem_index[i]+' '+problem_name[i]+'" prefix_auto="1" extension_auto="1" />\n'
          '				<Option object_output="obj/Debug/" />\n'
          '				<Option type="1" />\n'
          '				<Option compiler="gcc" />\n'
          '				<Compiler>\n'
          '					<Add option="-std=c++11" />\n'
          '					<Add option="-g" />\n'
          '				</Compiler>\n'
          '			</Target>\n'
          '			<Target title="Release">\n'
          '				<Option output="bin/Release/'+str(contest_id)+problem_index[i]+' '+problem_name[i]+'" prefix_auto="1" extension_auto="1" />\n'
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
          '		<Unit filename="main.cpp" />\n'
          '		<Extensions>\n'
          '			<code_completion />\n'
          '			<envvars />\n'
          '			<debugger />\n'
          '		</Extensions>\n'
          '	</Project>\n'
          '</CodeBlocks_project_file>\n')
    return temp
