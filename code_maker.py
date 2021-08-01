import path_maker
import string_manip
import name_maker
import strings

def code_cpp(self,tp):
    if(tp==strings.tp_main or tp==strings.tp_bf):
        return ('#include <bits/stdc++.h>\n'
                '\n'
                'using namespace std;\n'
                'typedef long long ll;\n'
                '\n'
                'int main()\n'
                '{\n'
                '    ios::sync_with_stdio(0);\n'
                '    cin.tie(0);\n'
                '    \n'
                '    return 0;\n'
                '}\n')
    elif(tp==strings.tp_ch):
        return ('#include <bits/stdc++.h>\n'
                '\n'
                'using namespace std;\n'
                'typedef long long ll;\n'
                '/*\n'
                'Input:\n'
                'gen.txt + main.txt\n'
                '\n'
                'Return:\n'
                'out_ok() if correct\n'
                'out_wa() if wrong\n'
                'Do NOT print anything else\n'
                '*/\n'
                'void out_ok(){exit(0);}\n'
                'void out_wa(string s=""){if(s=="") s="None"; cout << s << "\\n"; exit(0);}\n'
                '\n'
                'int main()\n'
                '{\n'
                '    ios::sync_with_stdio(0);\n'
                '    cin.tie(0);\n'
                '    \n'
                '    return 0;\n'
                '}\n')
    elif(tp==strings.tp_gen):
        return ('#include <bits/stdc++.h>\n'
                '\n'
                'using namespace std;\n'
                'typedef long long ll;\n'
                '\n'
                'mt19937 gen(chrono::steady_clock::now().time_since_epoch().count());\n'
                'mt19937_64 genll(chrono::steady_clock::now().time_since_epoch().count());\n'
                '\n'
                'int rng(int l,int r){return uniform_int_distribution<int>(l,r)(gen);}\n'
                'll rngll(ll l,ll r){return uniform_int_distribution<ll>(l,r)(genll);}\n'
                'void rng_shuffle(auto &v){shuffle(v.begin(),v.end(),gen);}\n'
                '\n'
                'int main()\n'
                '{\n'
                '    ios::sync_with_stdio(0);\n'
                '    cin.tie(0);\n'
                '    int tid; //id of current stress/check gen call, can be ignored, 1-indexed\n'
                '    cin >> tid;\n'
                '    \n'
                '    return 0;\n'
                '}\n')

def code_cbp(self,tp):
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n'
            '<CodeBlocks_project_file>\n'
            '    <FileVersion major="1" minor="6" />\n'
            '    <Project>\n'
            '        <Option title="'+name_maker.name_problem_cbp(self,tp)[:-4]+'" />\n'
            '        <Option pch_mode="2" />\n'
            '        <Option compiler="gcc" />\n'
            '        <Build>\n'
            '            <Target title="Debug">\n'
            '                <Option output="bin/Debug/'+name_maker.name_problem_cbp(self,tp)[:-4]+'" prefix_auto="1" extension_auto="1" />\n'
            '                <Option object_output="obj/Debug/" />\n'
            '                <Option type="1" />\n'
            '                <Option compiler="gcc" />\n'
            '                <Compiler>\n'
            '                    <Add option="-g" />\n'
            '                </Compiler>\n'
            '            </Target>\n'
            '            <Target title="Release">\n'
            '                <Option output="bin/Release/'+name_maker.name_problem_cbp(self,tp)[:-4]+'" prefix_auto="1" extension_auto="1" />\n'
            '                <Option object_output="obj/Release/" />\n'
            '                <Option type="1" />\n'
            '                <Option compiler="gcc" />\n'
            '                <Compiler>\n'
            '                    <Add option="-O2" />\n'
            '                </Compiler>\n'
            '                <Linker>\n'
            '                    <Add option="-s" />\n'
            '                </Linker>\n'
            '            </Target>\n'
            '        </Build>\n'
            '        <Compiler>\n'
            '            <Add option="-Wall" />\n'
            '            <Add option="-fexceptions" />\n'
            '        </Compiler>\n'
            '        <Unit filename="'+name_maker.name_problem_cpp(self,tp)+'" />\n'
            '        <Extensions>\n'
            '            <lib_finder disable_auto="1" />\n'
            '        </Extensions>\n'
            '    </Project>\n'
            '</CodeBlocks_project_file>\n')

def code_run(self):
    return (r'path_code=${1}''\n'
            r'path_io=${2}''\n'
            r'path_utils=${3}''\n'
            r'main=${4}''\n'
            r'out_main=${5}''\n'
            r'err_main=${6}''\n'
            r'problem_index=${7}''\n'
            r'io_cnt=${8}''\n'
            r'tl=${9}''\n'
            r'runbf=${10}''\n'
            r'NoColor="\033[0m"''\n'
            r'BRed="\033[1;31m"''\n'
            r'BGreen="\033[1;32m"''\n'
            r'BYellow="\033[1;33m"''\n'
            r'BBlue="\033[1;34m"''\n'
            r'BPurple="\033[1;35m"''\n'
            r'BWhite="\033[1;37m"''\n'
            r'clean() { printf "${NoColor}\n"; exit 0; }''\n'
            r'trap clean SIGINT''\n'
            r'ulimit -s unlimited''\n'
            r'cd "${path_code}"''\n'
            r'if ! g++ -Wall -Wextra -Wshadow -std=c++17 -O2 "${main}.cpp" -o "${main}"''\n'
            r'then''\n'
            r'    printf "${BWhite}CE${NoColor}\n"''\n'
            r'    exit 0''\n'
            r'fi''\n'
            r'for((i=1;i<=${io_cnt};i++))''\n'
            r'do''\n'
            r'    printf "${BWhite}[Test${runbf} #${i}] ${NoColor}"''\n'
            r'    { timeout --foreground ${tl} "./${main}" < "${path_io}/${problem_index}_${i}.in" > "${path_io}/${out_main}"; } &> "${path_utils}/${err_main}"''\n'
            r'    if((${?}==124))''\n'
            r'    then''\n'
            r'        printf "${BPurple}TLE${NoColor}\n"''\n'
            r'    elif [[ -s "${path_utils}/${err_main}" ]]''\n'
            r'    then''\n'
            r'        printf "${BYellow}RTE${NoColor}\n"''\n'
            r'    elif cmp -s <(tr -s [:space:] " " < <(cat <(printf " ") "${path_io}/${out_main}" <(printf " "))) <(tr -s [:space:] " " < <(cat <(printf " ") "${path_io}/${problem_index}_${i}.out" <(printf " ")))''\n'
            r'    then''\n'
            r'        printf "${BGreen}OK${NoColor}\n"''\n'
            r'    else''\n'
            r'        printf "${BRed}WA${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${problem_index}_${i}.in")"''\n'
            r'        printf "${BBlue}Received${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_main}")"''\n'
            r'        printf "${BBlue}Expected${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${problem_index}_${i}.out")"''\n'
            r'    fi''\n'
            r'done''\n')

def code_stress(self):
    return (r'path_code=${1}''\n'
            r'path_io=${2}''\n'
            r'path_utils=${3}''\n'
            r'main=${4}''\n'
            r'out_main=${5}''\n'
            r'err_main=${6}''\n'
            r'bf=${7}''\n'
            r'out_bf=${8}''\n'
            r'err_bf=${9}''\n'
            r'gen=${10}''\n'
            r'out_gen=${11}''\n'
            r'err_gen=${12}''\n'
            r'stress_cnt=${13}''\n'
            r'tl=${14}''\n'
            r'out_verdict=${15}''\n'
            r'regen=${16}''\n'
            r'NoColor="\033[0m"''\n'
            r'BRed="\033[1;31m"''\n'
            r'BGreen="\033[1;32m"''\n'
            r'BYellow="\033[1;33m"''\n'
            r'BBlue="\033[1;34m"''\n'
            r'BPurple="\033[1;35m"''\n'
            r'BWhite="\033[1;37m"''\n'
            r'clean() { printf "${NoColor}\n"; exit 0; }''\n'
            r'trap clean SIGINT''\n'
            r'ulimit -s unlimited''\n'
            r'cd "${path_code}"''\n'
            r'> "${path_utils}/${out_verdict}"''\n'
            r'if ! g++ -Wall -Wextra -Wshadow -std=c++17 -O2 "${main}.cpp" -o "${main}"''\n'
            r'then''\n'
            r'    printf "${BWhite}CE${NoColor}\n"''\n'
            r'    exit 0''\n'
            r'fi''\n'
            r'if ! g++ -Wall -Wextra -Wshadow -std=c++17 -O2 "${bf}.cpp" -o "${bf}"''\n'
            r'then''\n'
            r'    printf "${BWhite}CE: bf${NoColor}\n"''\n'
            r'    exit 0''\n'
            r'fi''\n'
            r'if ! g++ -Wall -Wextra -Wshadow -std=c++17 -O2 "${gen}.cpp" -o "${gen}"''\n'
            r'then''\n'
            r'    printf "${BWhite}CE: gen${NoColor}\n"''\n'
            r'    exit 0''\n'
            r'fi''\n'
            r'for((i=1;i<=${stress_cnt};i++))''\n'
            r'do''\n'
            r'    if [[ -z "${regen}" ]]''\n'
            r'    then''\n'
            r'        { timeout --foreground ${tl} "./${gen}" < <(printf "${i}") > "${path_io}/${out_gen}"; } &> "${path_utils}/${err_gen}"''\n'
            r'        if((${?}==124))''\n'
            r'        then''\n'
            r'            printf "\r${BWhite}[Stress${regen} #${i}] ${BPurple}TLE: gen${NoColor}\n"''\n'
            r'            break''\n'
            r'        elif [[ -s "${path_utils}/${err_gen}" ]]''\n'
            r'        then''\n'
            r'            printf "\r${BWhite}[Stress${regen} #${i}] ${BYellow}RTE: gen${NoColor}\n"''\n'
            r'            break''\n'
            r'        fi''\n'
            r'    fi''\n'
            r'    { timeout --foreground ${tl} "./${bf}" < "${path_io}/${out_gen}" > "${path_io}/${out_bf}"; } &> "${path_utils}/${err_bf}"''\n'
            r'    if((${?}==124))''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Stress${regen} #${i}] ${BPurple}TLE: bf${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        break''\n'
            r'    elif [[ -s "${path_utils}/${err_bf}" ]]''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Stress${regen} #${i}] ${BYellow}RTE: bf${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        break''\n'
            r'    fi''\n'
            r'    { timeout --foreground ${tl} "./${main}" < "${path_io}/${out_gen}" > "${path_io}/${out_main}"; } &> "${path_utils}/${err_main}"''\n'
            r'    if((${?}==124))''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Stress${regen} #${i}] ${BPurple}TLE${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "${BBlue}Expected${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_bf}")"''\n'
            r'        printf "TLE" > "${path_utils}/${out_verdict}"''\n'
            r'        break''\n'
            r'    elif [[ -s "${path_utils}/${err_main}" ]]''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Stress${regen} #${i}] ${BYellow}RTE${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "${BBlue}Expected${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_bf}")"''\n'
            r'        printf "RTE" > "${path_utils}/${out_verdict}"''\n'
            r'        break''\n'
            r'    fi''\n'
            r'    if diff -q -b -B "${path_io}/${out_main}" "${path_io}/${out_bf}" &> /dev/null''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Stress${regen} #${i}] ${BGreen}OK${NoColor}"''\n'
            r'        printf "OK" > "${path_utils}/${out_verdict}"''\n'
            r'        if((i==${stress_cnt}))''\n'
            r'        then''\n'
            r'            printf "${NoColor}\n"''\n'
            r'        fi''\n'
            r'    else''\n'
            r'        printf "\r${BWhite}[Stress${regen} #${i}] ${BRed}WA${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "${BBlue}Received${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_main}")"''\n'
            r'        printf "${BBlue}Expected${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_bf}")"''\n'
            r'        printf "WA" > "${path_utils}/${out_verdict}"''\n'
            r'        break''\n'
            r'    fi''\n'
            r'done''\n')

def code_check(self):
    return (r'path_code=${1}''\n'
            r'path_io=${2}''\n'
            r'path_utils=${3}''\n'
            r'main=${4}''\n'
            r'out_main=${5}''\n'
            r'err_main=${6}''\n'
            r'ch=${7}''\n'
            r'out_ch=${8}''\n'
            r'err_ch=${9}''\n'
            r'gen=${10}''\n'
            r'out_gen=${11}''\n'
            r'err_gen=${12}''\n'
            r'check_cnt=${13}''\n'
            r'tl=${14}''\n'
            r'out_verdict=${15}''\n'
            r'regen=${16}''\n'
            r'NoColor="\033[0m"''\n'
            r'BRed="\033[1;31m"''\n'
            r'BGreen="\033[1;32m"''\n'
            r'BYellow="\033[1;33m"''\n'
            r'BBlue="\033[1;34m"''\n'
            r'BPurple="\033[1;35m"''\n'
            r'BWhite="\033[1;37m"''\n'
            r'clean() { printf "${NoColor}\n"; exit 0; }''\n'
            r'trap clean SIGINT''\n'
            r'ulimit -s unlimited''\n'
            r'cd "${path_code}"''\n'
            r'> "${path_utils}/${out_verdict}"''\n'
            r'if ! g++ -Wall -Wextra -Wshadow -std=c++17 -O2 "${main}.cpp" -o "${main}"''\n'
            r'then''\n'
            r'    printf "${BWhite}CE${NoColor}\n"''\n'
            r'    exit 0''\n'
            r'fi''\n'
            r'if ! g++ -Wall -Wextra -Wshadow -std=c++17 -O2 "${ch}.cpp" -o "${ch}"''\n'
            r'then''\n'
            r'    printf "${BWhite}CE: ch${NoColor}\n"''\n'
            r'    exit 0''\n'
            r'fi''\n'
            r'if ! g++ -Wall -Wextra -Wshadow -std=c++17 -O2 "${gen}.cpp" -o "${gen}"''\n'
            r'then''\n'
            r'    printf "${BWhite}CE: gen${NoColor}\n"''\n'
            r'    exit 0''\n'
            r'fi''\n'
            r'for((i=1;i<=${check_cnt};i++))''\n'
            r'do''\n'
            r'    if [[ -z "${regen}" ]]''\n'
            r'    then''\n'
            r'        { timeout --foreground ${tl} "./${gen}" < <(printf "${i}") > "${path_io}/${out_gen}"; } &> "${path_utils}/${err_gen}"''\n'
            r'        if((${?}==124))''\n'
            r'        then''\n'
            r'            printf "\r${BWhite}[Stress #${i}] ${BPurple}TLE: gen${NoColor}\n"''\n'
            r'            break''\n'
            r'        elif [[ -s "${path_utils}/${err_gen}" ]]''\n'
            r'        then''\n'
            r'            printf "\r${BWhite}[Stress #${i}] ${BYellow}RTE: gen${NoColor}\n"''\n'
            r'            break''\n'
            r'        fi''\n'
            r'    fi''\n'
            r'    { timeout --foreground ${tl} "./${main}" < "${path_io}/${out_gen}" > "${path_io}/${out_main}"; } &> "${path_utils}/${err_main}"''\n'
            r'    if((${?}==124))''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Check${regen} #${i}] ${BPurple}TLE${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "TLE" > "${path_utils}/${out_verdict}"''\n'
            r'        break''\n'
            r'    elif [[ -s "${path_utils}/${err_main}" ]]''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Check${regen} #${i}] ${BYellow}RTE${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "RTE" > "${path_utils}/${out_verdict}"''\n'
            r'        break''\n'
            r'    fi''\n'
            r'    { timeout --foreground ${tl} "./${ch}" < <(cat "${path_io}/${out_gen}" "${path_io}/${out_main}") > "${path_io}/${out_ch}"; } &> "${path_utils}/${err_ch}"''\n'
            r'    if((${?}==124))''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Check${regen} #${i}] ${BPurple}TLE: ch${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "${BBlue}Received${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_main}")"''\n'
            r'        break''\n'
            r'    elif [[ -s "${path_utils}/${err_ch}" ]]''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Check${regen} #${i}] ${BYellow}RTE: ch${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "${BBlue}Received${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_main}")"''\n'
            r'        break''\n'
            r'    fi''\n'
            r'    if [[ ! -s "${path_io}/${out_ch}" ]]''\n'
            r'    then''\n'
            r'        printf "\r${BWhite}[Check${regen} #${i}] ${BGreen}OK${NoColor}"''\n'
            r'        printf "OK" > "${path_utils}/${out_verdict}"''\n'
            r'        if((i==${check_cnt}))''\n'
            r'        then''\n'
            r'            printf "${NoColor}\n"''\n'
            r'        fi''\n'
            r'    else''\n'
            r'        printf "\r${BWhite}[Check${regen} #${i}] ${BRed}WA${NoColor}\n"''\n'
            r'        printf "${BBlue}Input${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_gen}")"''\n'
            r'        printf "${BBlue}Received${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_main}")"''\n'
            r'        printf "${BBlue}Checker Log${NoColor}\n"''\n'
            r'        echo "$(<"${path_io}/${out_ch}")"''\n'
            r'        printf "WA" > "${path_utils}/${out_verdict}"''\n'
            r'        break''\n'
            r'    fi''\n'
            r'done''\n')

def code_dbg(self,tp):
    compile_command='cd '+string_manip.path_win_q(path_maker.path_problem(self))+' && g++ -g -Wall -Wextra -Wshadow -std=c++17 -Wl,--stack,1000000000 '+string_manip.quotify(name_maker.name_problem_cpp(self,tp))+' -o '+string_manip.quotify(name_maker.name_problem_dbg(self,tp))
    gdb_command='start cmd /c "'+'cd '+string_manip.path_win_q(path_maker.path_problem(self))+' && gdb '+'\\"'+name_maker.name_problem_dbg(self,tp)+'\\"'+'"'
    return [compile_command,gdb_command]
