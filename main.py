from output_setup import printf
import contest_info
import website_source
import file_management
import strings
import prompt_handling

contest_id=prompt_handling.prompt_contest_id();
if(not contest_info.contest_exists(contest_id)):
    prompt_handling.prompt_contest_does_not_exist()

contest_info.get_problems(contest_id)
problem_index=contest_info.problem_index
problem_name=contest_info.problem_name
for i in range(len(problem_index)):
    print(problem_index[i]+' '+problem_name[i])

if(not file_management.file_exists(strings.path+str(contest_id))):
    file_management.create_folder(strings.path+str(contest_id))
    for i in range(len(problem_index)):
        problem_path=strings.path+str(contest_id)+'\\'+str(contest_id)+problem_index[i]+' '+problem_name[i]
        problem_path_name=str(contest_id)+problem_index[i]+' '+problem_name[i]
        file_management.create_folder(problem_path)
        file_management.create_file(problem_path+'\\main.cpp',strings.code_cpp)
        file_management.create_file(problem_path+'\\'+problem_path_name+'.cbp',strings.code_cb1+problem_path_name+strings.code_cb2+problem_path_name+strings.code_cb3+problem_path_name+strings.code_cb4)
