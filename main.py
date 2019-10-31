import strings
import path_maker
import code_maker
import string_manip
import checker
import contest_create
import contest_info
import website_source
import file_management
import system_action
import output_setup
import prompt_handling

contest_id=prompt_handling.prompt_contest_id()
if(not file_management.file_exists(path_maker.path_contest(contest_id))):
    if(not contest_info.contest_exists(contest_id)):
        prompt_handling.prompt_contest_does_not_exist()
    contest_info.get_problems_online(contest_id)
    contest_create.init()
    path_maker.init()
    code_maker.init()
    checker.init()
    contest_create.create_contest(contest_id)
    prompt_handling.prompt_succesful_parsing()
    system_action.run_batch(path_maker.path_temp_cmd(contest_id))
else:
    contest_info.get_problems_offline(contest_id)
    contest_create.init()
    path_maker.init()
    code_maker.init()
    checker.init()
    prompt_handling.prompt_already_parsed()
    if(prompt_handling.prompt_optional_cbopener()):
        system_action.run_batch(path_maker.path_temp_cmd(contest_id))

prompt_handling.prompt_newline(1)

problem_index=contest_info.problem_index
last_valid=0
commands=[strings.command_path,strings.command_exit]

while(1):
    problem_index_checker=prompt_handling.prompt_problem_index_checker()
    if(problem_index_checker.upper() in problem_index):
        checker.problem_checker(contest_id,problem_index.index(problem_index_checker.upper()))
        last_valid=problem_index.index(problem_index_checker.upper())
    elif(problem_index_checker in commands):
        if(problem_index_checker==strings.command_path):
            system_action.copy_to_clipboard(path_maker.path_problem_main(contest_id,last_valid))
        elif(problem_index_checker==strings.command_exit):
            break
    else:
        prompt_handling.prompt_unrecognized_problem_index(problem_index_checker)
    prompt_handling.prompt_newline(1)
