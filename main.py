from output_setup import printf
import contest_info
import website_source
import file_management
import strings
import prompt_handling
import contest_create
import checker
import path_maker

contest_id=prompt_handling.prompt_contest_id()
if(not contest_info.contest_exists(contest_id)):
    prompt_handling.prompt_contest_does_not_exist()

contest_info.get_problems(contest_id)
problem_index=contest_info.problem_index
problem_name=contest_info.problem_name

if(not file_management.file_exists(path_maker.path_contest(contest_id))):
    contest_create.create_contest(contest_id)

prompt_handling.prompt_succesful_parsing()

while(1):
    problem_index_checker=prompt_handling.prompt_problem_index_checker()
    if(not ((problem_index_checker in problem_index) or problem_index_checker==strings.command_exit)):
        prompt_handling.prompt_unrecognized_problem_index(problem_index_checker)
    elif(problem_index_checker==strings.command_exit):
        break
    else:
        checker.problem_checker(contest_id,problem_index.index(problem_index_checker))
