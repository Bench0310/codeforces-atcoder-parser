import strings
import file_management
import contest_info

problem_index=contest_info.problem_index
problem_name=contest_info.problem_name

def create_contest(contest_id):
    file_management.create_folder(strings.path+str(contest_id))
    for i in range(len(problem_index)):
        problem_path=strings.path+str(contest_id)+'\\'+str(contest_id)+problem_index[i]+' '+problem_name[i]
        problem_path_name=str(contest_id)+problem_index[i]+' '+problem_name[i]
        file_management.create_folder(problem_path)
        file_management.create_file(problem_path+'\\main.cpp',strings.code_cpp)
        file_management.create_file(problem_path+'\\'+problem_path_name+'.cbp',strings.code_cb1+problem_path_name+strings.code_cb2+problem_path_name+strings.code_cb3+problem_path_name+strings.code_cb4)
