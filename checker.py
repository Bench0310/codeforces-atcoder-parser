import subprocess
import contest_info
import file_management
import strings
import prompt_handling
import path_maker

problem_index=contest_info.problem_index
sample_test_in=contest_info.sample_test_in

def problem_checker(contest_id,i):
    global problem_index
    global sample_test_in
    subprocess.call(path_maker.path_checker_cmd(contest_id,i))
    for j in range(len(sample_test_in[i])):
        sample_test_output=file_management.read_file(path_maker.path_checker_output(contest_id,i,j+1))
        sample_test_answer=file_management.read_file(path_maker.path_io_out(contest_id,i,j+1))
        sample_test_output=sample_test_output.replace(' \n','\n')
        if(sample_test_output==sample_test_answer):
            prompt_handling.prompt_test_status(j+1,'OK')
        else:
            prompt_handling.prompt_test_status(j+1,'WA')
            prompt_handling.prompt_output_comparison(sample_test_output,sample_test_answer)
    prompt_handling.prompt_newline(3)
