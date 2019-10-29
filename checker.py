import subprocess
import contest_info
import file_management
import strings
import prompt_handling

problem_index=contest_info.problem_index
sample_test_in=contest_info.sample_test_in

def problem_checker(contest_id,i):
    global problem_index
    global sample_test_in
    subprocess.call(strings.path+str(contest_id)+'\\'+'Checker'+'\\'+'_'+problem_index[i]+'.cmd')
    for j in range(len(sample_test_in[i])):
        sample_test_output=file_management.read_file(strings.path+str(contest_id)+'\\'+'Checker'+'\\'+problem_index[i]+'_'+f'{(j+1):02d}'+'_output.txt')
        sample_test_answer=file_management.read_file(strings.path+str(contest_id)+'\\'+'IO'+'\\'+problem_index[i]+'_'+f'{(j+1):02d}'+'.out')
        sample_test_output=sample_test_output.replace(' \n','\n')
        if(sample_test_output==sample_test_answer):
            prompt_handling.prompt_test_status(j+1,'OK')
        else:
            prompt_handling.prompt_test_status(j+1,'WA')
            prompt_handling.prompt_output_comparison(sample_test_output,sample_test_answer)
    prompt_handling.prompt_newline(3)
