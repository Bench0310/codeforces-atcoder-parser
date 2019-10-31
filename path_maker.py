import contest_info
import string_manip

path='C:\\Bench\\CodeHub\\Codeforces'
delim='\\'

problem_index=[]
problem_name=[]

def init():
    global problem_index
    global problem_name
    problem_index=contest_info.problem_index
    problem_name=contest_info.problem_name

def path_contest(contest_id):
    return path+delim+str(contest_id)

def path_problem(contest_id,i):
    return path_contest(contest_id)+delim+str(contest_id)+problem_index[i]+' '+problem_name[i]

def path_problem_main(contest_id,i):
    return path_problem(contest_id,i)+delim+'main.cpp'

def path_problem_cbp(contest_id,i):
    return path_problem(contest_id,i)+delim+str(contest_id)+problem_index[i]+' '+problem_name[i]+'.cbp'

def path_io(contest_id):
    return path_contest(contest_id)+delim+'IO'

def path_io_in(contest_id,i,j):
    return path_io(contest_id)+delim+problem_index[i]+'_'+string_manip.k_digit(j,2)+'.in'

def path_io_out(contest_id,i,j):
    return path_io(contest_id)+delim+problem_index[i]+'_'+string_manip.k_digit(j,2)+'.out'

def path_checker(contest_id):
    return path_contest(contest_id)+delim+'Checker'

def path_checker_cmd(contest_id,i):
    return path_checker(contest_id)+delim+'_'+problem_index[i]+'.cmd'

def path_checker_cmd_problem_index(contest_id,i,j):
    return path_checker(contest_id)+delim+'_'+problem_index[i]+'_'+string_manip.k_digit(j,2)+'.cmd'

def path_checker_exe(contest_id,i):
    return path_checker(contest_id)+delim+problem_index[i]+'.exe'

def path_checker_output(contest_id,i,j):
    return path_checker(contest_id)+delim+problem_index[i]+'_'+string_manip.k_digit(j,2)+'_'+'output'+'.txt'

def path_temp(contest_id):
    return path_contest(contest_id)+delim+'temp'

def path_temp_cmd(contest_id):
    return path_temp(contest_id)+delim+'cbopenener'+'.cmd'

def path_temp_problem_index(contest_id):
    return path_temp(contest_id)+delim+'problem_index'+'.txt'

def path_temp_problem_name(contest_id):
    return path_temp(contest_id)+delim+'problem_name'+'.txt'

def path_temp_sample_test_num(contest_id):
    return path_temp(contest_id)+delim+'sample_test_num'+'.txt'
