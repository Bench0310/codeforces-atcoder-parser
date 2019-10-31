import contest_info
import file_management
import strings
import prompt_handling
import path_maker
import system_action

problem_index=[]
sample_test_num=[]

def init():
    global problem_index
    global sample_test_num
    problem_index=contest_info.problem_index
    sample_test_num=contest_info.sample_test_num

def problem_checker(contest_id,i):
    global problem_index
    global sample_test_in
    system_action.run_batch(path_maker.path_checker_cmd(contest_id,i))
    for j in range(sample_test_num[i]):
        prompt_handling.prompt_test(j+1)
        system_action.run_batch(path_maker.path_checker_cmd_problem_index(contest_id,i,j+1))
        sample_test_output=file_management.read_file(path_maker.path_checker_output(contest_id,i,j+1))
        sample_test_answer=file_management.read_file(path_maker.path_io_out(contest_id,i,j+1))
        sample_test_output=sample_test_output.replace(' \n','\n')
        if(sample_test_output==sample_test_answer):
            prompt_handling.prompt_test_status('OK')
        else:
            prompt_handling.prompt_test_status('WA')
            prompt_handling.prompt_output_comparison(sample_test_output,sample_test_answer)
    prompt_handling.prompt_newline(2)
