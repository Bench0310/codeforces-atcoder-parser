import strings
import file_management
import contest_info

problem_index=contest_info.problem_index
problem_name=contest_info.problem_name
sample_test_in=contest_info.sample_test_in
sample_test_out=contest_info.sample_test_out

def create_contest(contest_id):
    global problem_index
    global problem_name
    global sample_test_in
    global sample_test_out
    file_management.create_folder(strings.path+str(contest_id))
    for i in range(len(problem_index)):
        problem_path=strings.path+str(contest_id)+'\\'+str(contest_id)+problem_index[i]+' '+problem_name[i]
        problem_path_name=str(contest_id)+problem_index[i]+' '+problem_name[i]
        file_management.create_folder(problem_path)
        file_management.create_file(problem_path+'\\main.cpp',strings.code_cpp)
        file_management.create_file(problem_path+'\\'+problem_path_name+'.cbp',strings.code_cb1+problem_path_name+strings.code_cb2+problem_path_name+strings.code_cb3+problem_path_name+strings.code_cb4)
    io_path=strings.path+str(contest_id)+'\\'+'IO'
    file_management.create_folder(io_path)
    for i in range(len(problem_index)):
        for j in range(len(sample_test_in[i])):
            file_management.create_file(io_path+'\\'+problem_index[i]+'_'+f'{(j+1):02d}'+'.in',sample_test_in[i][j])
            file_management.create_file(io_path+'\\'+problem_index[i]+'_'+f'{(j+1):02d}'+'.out',sample_test_out[i][j])
    checker_path=strings.path+str(contest_id)+'\\'+'Checker'
    file_management.create_folder(checker_path)
    for i in range(len(problem_index)):
        checker_code=strings.code_cmd1+strings.code_cmd2+checker_path+'\n'+strings.code_cmd3+problem_index[i]+' '+'"'+strings.path+str(contest_id)+'\\'+str(contest_id)+problem_index[i]+' '+problem_name[i]+'\\'+'main.cpp'+'"'+'\n'
        for j in range(len(sample_test_in[i])):
            checker_code+=problem_index[i]+'.exe'+' < '+io_path+'\\'+problem_index[i]+'_'+f'{(j+1):02d}'+'.in'+' > '+problem_index[i]+'_'+f'{(j+1):02d}'+'_output.txt'+'\n'
        file_management.create_file(checker_path+'\\'+'_'+problem_index[i]+'.cmd',checker_code)
