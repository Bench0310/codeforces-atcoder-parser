import path_maker
import string_manip
import name_maker
import strings

def code_cpp(self,tp):
    if(tp==strings.main or tp==strings.bf):
        temp=('#include <bits/stdc++.h>\n'
              '\n'
              'using namespace std;\n'
              '\n'
              'int main()\n'
              '{\n'
              '    \n'
              '    return 0;\n'
              '}\n')
    elif(tp==strings.ch):
        temp=('#include <bits/stdc++.h>\n'
              '\n'
              'using namespace std;\n'
              '/*\n'
              'Input:\n'
              'gen.txt + main.txt\n'
              '\n'
              'Return:\n'
              'out("OK") if correct\n'
              'out("WA") if wrong\n'
              'Do NOT print anything else\n'
              '*/\n'
              'void out(string s)\n'
              '{\n'
              '    if(s!="OK"&&s!="WA") abort();\n'
              '    cout << s;\n'
              '    exit(0);\n'
              '}\n'
              '\n'
              'int main()\n'
              '{\n'
              '    \n'
              '    return 0;\n'
              '}\n'
              '\n')
    elif(tp==strings.gen):
        temp=('#include <bits/stdc++.h>\n'
              '\n'
              'using namespace std;\n'
              '/*\n'
              'Random int:\n'
              'uniform_int_distribution<int>(,)(rng)\n'
              '\n'
              'Random long long:\n'
              'uniform_int_distribution<long long>(,)(rngll)\n'
              '\n'
              'Random permutation:\n'
              'shuffle(,,rng);\n'
              '*/\n'
              'mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());\n'
              'mt19937_64 rngll(chrono::steady_clock::now().time_since_epoch().count());\n'
              '\n'
              'int main()\n'
              '{\n'
              '    \n'
              '    return 0;\n'
              '}\n'
              '\n')
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
          '					<Add option="-Wshadow" />\n'
          '					<Add option="-Wextra" />\n'
          '					<Add option="-Wall" />\n'
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

def code_run(self):
    temp=('# $1 -> io_cnt\n'
          '# $2 -> tl\n'
          'NoColor=\'\\033[0m\'\n'
          'BRed=\'\\033[1;31m\'\n'
          'BGreen=\'\\033[1;32m\'\n'
          'BBlue=\'\\033[1;34m\'\n'
          'BPurple=\'\\033[1;35m\'\n'
          'BWhite=\'\\033[1;37m\'\n'
          'g++ -Wall -Wextra -Wshadow -std=c++17 '+string_manip.path_wsl_q(path_maker.path_problem_cpp(self,strings.main))+' -o '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.main))+'\n'
          'for((i=1;i<=${1};i++))\n'
          'do\n'
          '    printf "${BWhite}[Test #${i}] "\n'
          '    timeout ${2} '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.main))+' < "'+string_manip.path_wsl(path_maker.path_io(self))+'/'+self.problem_index+'_${i}.in" > '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+'\n'
          '    if((${?}==124))\n'
          '    then\n'
          '        printf "${BPurple}TLE${NoColor}\\n"\n'
          '    elif [[ ! $(diff -w '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+' "'+string_manip.path_wsl(path_maker.path_io(self))+'/'+self.problem_index+'_${i}.out") ]]\n'
          '    then\n'
          '        printf "${BGreen}OK${NoColor}\\n"\n'
          '    else\n'
          '        printf "${BRed}WA${NoColor}\\n"\n'
          '        printf "${BBlue}Input${NoColor}\\n"\n'
          '        cat "'+string_manip.path_wsl(path_maker.path_io(self))+'/'+self.problem_index+'_${i}.in"\n'
          '        printf "${BBlue}Received${NoColor}\\n"\n'
          '        cat '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+'\n'
          '        printf "${BBlue}Expected${NoColor}\\n"\n'
          '        cat "'+string_manip.path_wsl(path_maker.path_io(self))+'/'+self.problem_index+'_${i}.out"\n'
          '    fi\n'
          'done\n'
          '\n')
    return temp

def code_stress(self):
    temp=('# $1 -> stress_cnt\n'
          '# $2 -> tl\n'
          'NoColor=\'\\033[0m\'\n'
          'BRed=\'\\033[1;31m\'\n'
          'BGreen=\'\\033[1;32m\'\n'
          'BBlue=\'\\033[1;34m\'\n'
          'BPurple=\'\\033[1;35m\'\n'
          'BWhite=\'\\033[1;37m\'\n'
          'g++ -Wall -Wextra -Wshadow -std=c++17 '+string_manip.path_wsl_q(path_maker.path_problem_cpp(self,strings.main))+' -o '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.main))+'\n'
          'g++ -Wall -Wextra -Wshadow -std=c++17 '+string_manip.path_wsl_q(path_maker.path_problem_cpp(self,strings.bf))+' -o '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.bf))+'\n'
          'g++ -Wall -Wextra -Wshadow -std=c++17 '+string_manip.path_wsl_q(path_maker.path_problem_cpp(self,strings.gen))+' -o '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.gen))+'\n'
          'for((i=1;i<=${1};i++))\n'
          'do\n'
          '    timeout ${2} '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.gen))+' > '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+'\n'
          '    if((${?}==124))\n'
          '    then\n'
          '        printf "\\r${BWhite}[Stress #${i}] ${BPurple}TLE: gen${NoColor}\\n"\n'
          '        printf "TLE" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          '    timeout ${2} '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.main))+' < '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+' > '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+'\n'
          '    if((${?}==124))\n'
          '    then\n'
          '        printf "\\r${BWhite}[Stress #${i}] ${BPurple}TLE${NoColor}\\n"\n'
          '        printf "TLE" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          '    timeout ${2} '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.bf))+' < '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+' > '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.bf))+'\n'
          '    if((${?}==124))\n'
          '    then\n'
          '        printf "\\r${BWhite}[Stress #${i}] ${BPurple}TLE: bf${NoColor}\\n"\n'
          '        printf "TLE" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          '    if [[ ! $(diff -w '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+' '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.bf))+') ]]\n'
          '    then\n'
          '        printf "\\r${BWhite}[Stress #${i}] ${BGreen}OK${NoColor}"\n'
          '        printf "OK" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        if((i==${1}))\n'
          '        then\n'
          '            printf "${NoColor}\\n"\n'
          '        fi\n'
          '    else\n'
          '        printf "\\r${BWhite}[Stress #${i}] ${BRed}WA${NoColor}\\n"\n'
          '        printf "${BBlue}Input${NoColor}\\n"\n'
          '        cat '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+'\n'
          '        printf "${BBlue}Received${NoColor}\\n"\n'
          '        cat '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+'\n'
          '        printf "${BBlue}Expected${NoColor}\\n"\n'
          '        cat '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.bf))+'\n'
          '        printf "WA" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          'done\n'
          '\n')
    return temp

def code_check(self):
    temp=('# $1 -> check_cnt\n'
          '# $2 -> tl\n'
          'NoColor=\'\\033[0m\'\n'
          'BRed=\'\\033[1;31m\'\n'
          'BGreen=\'\\033[1;32m\'\n'
          'BBlue=\'\\033[1;34m\'\n'
          'BPurple=\'\\033[1;35m\'\n'
          'BWhite=\'\\033[1;37m\'\n'
          'g++ -Wall -Wextra -Wshadow -std=c++17 '+string_manip.path_wsl_q(path_maker.path_problem_cpp(self,strings.main))+' -o '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.main))+'\n'
          'g++ -Wall -Wextra -Wshadow -std=c++17 '+string_manip.path_wsl_q(path_maker.path_problem_cpp(self,strings.ch))+' -o '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.ch))+'\n'
          'g++ -Wall -Wextra -Wshadow -std=c++17 '+string_manip.path_wsl_q(path_maker.path_problem_cpp(self,strings.gen))+' -o '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.gen))+'\n'
          'for((i=1;i<=${1};i++))\n'
          'do\n'
          '    timeout ${2} '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.gen))+' > '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+'\n'
          '    if((${?}==124))\n'
          '    then\n'
          '        printf "\\r${BWhite}[Check #${i}] ${BPurple}TLE: gen${NoColor}\\n"\n'
          '        printf "TLE" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          '    timeout ${2} '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.main))+' < '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+' > '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+'\n'
          '    if((${?}==124))\n'
          '    then\n'
          '        printf "\\r${BWhite}[Check #${i}] ${BPurple}TLE${NoColor}\\n"\n'
          '        printf "TLE" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          '    timeout ${2} '+string_manip.path_wsl_q(path_maker.path_problem_exe(self,strings.ch))+' < <(cat '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+' '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+') > '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.ch))+'\n'
          '    if((${?}==124))\n'
          '    then\n'
          '        printf "\\r${BWhite}[Check #${i}] ${BPurple}TLE: ch${NoColor}\\n"\n'
          '        printf "TLE" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          '    ok="$(<'+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.ch))+')"\n'
          '    if [[ "${ok}" == "OK" ]]\n'
          '    then\n'
          '        printf "\\r${BWhite}[Check #${i}] ${BGreen}OK${NoColor}"\n'
          '        printf "OK" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        if((i==${1}))\n'
          '        then\n'
          '            printf "${NoColor}\\n"\n'
          '        fi\n'
          '    else\n'
          '        printf "\\r${BWhite}[Check #${i}] ${BRed}WA${NoColor}\\n"\n'
          '        printf "${BBlue}Input${NoColor}\\n"\n'
          '        cat '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.gen))+'\n'
          '        printf "${BBlue}Received${NoColor}\\n"\n'
          '        cat '+string_manip.path_wsl_q(path_maker.path_io_txt(self,strings.main))+'\n'
          '        printf "WA" > '+string_manip.path_wsl_q(path_maker.path_utils_verdict(self))+'\n'
          '        break\n'
          '    fi\n'
          'done\n'
          '\n')
    return temp
