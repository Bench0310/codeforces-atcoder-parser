import strings
import file_management
import contest_info
import path_maker
import code_maker

problem_index=[]
problem_name=[]
sample_test_in=[]
sample_test_out=[]

def init():
    global problem_index
    global problem_name
    global sample_test_in
    global sample_test_out
    problem_index=contest_info.problem_index
    problem_name=contest_info.problem_name
    sample_test_in=contest_info.sample_test_in
    sample_test_out=contest_info.sample_test_out

def create_contest(contest_id):
    file_management.create_folder(path_maker.path_contest(contest_id))
    for i in range(len(problem_index)):
        file_management.create_folder(path_maker.path_problem(contest_id,i))
        file_management.create_file(path_maker.path_problem_main(contest_id,i),code_maker.code_main())
        file_management.create_file(path_maker.path_problem_cbp(contest_id,i),code_maker.code_cbp(contest_id,i))
    file_management.create_folder(path_maker.path_io(contest_id))
    for i in range(len(problem_index)):
        for j in range(len(sample_test_in[i])):
            file_management.create_file(path_maker.path_io_in(contest_id,i,j+1),sample_test_in[i][j])
            file_management.create_file(path_maker.path_io_out(contest_id,i,j+1),sample_test_out[i][j])
    file_management.create_folder(path_maker.path_checker(contest_id))
    for i in range(len(problem_index)):
        file_management.create_file(path_maker.path_checker_cmd(contest_id,i),code_maker.code_cmd(contest_id,i))
        for j in range(len(sample_test_in[i])):
            file_management.create_file(path_maker.path_checker_cmd_problem_index(contest_id,i,j+1),code_maker.code_cmd_problem_index(contest_id,i,j+1))
    file_management.create_folder(path_maker.path_temp(contest_id))
    file_management.create_file(path_maker.path_temp_problem_index(contest_id),code_maker.code_problem_index())
    file_management.create_file(path_maker.path_temp_problem_name(contest_id),code_maker.code_problem_name())
    file_management.create_file(path_maker.path_temp_sample_test_num(contest_id),code_maker.code_sample_test_num())
    file_management.create_file(path_maker.path_temp_cmd(contest_id),code_maker.code_cb_opener(contest_id))
