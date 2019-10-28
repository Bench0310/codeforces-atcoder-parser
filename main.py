from output_setup import printf
import contest_info
import website_source
import file_management
import strings
import prompt_handling
import contest_create

contest_id=prompt_handling.prompt_contest_id();
if(not contest_info.contest_exists(contest_id)):
    prompt_handling.prompt_contest_does_not_exist()

contest_info.get_problems(contest_id)
problem_index=contest_info.problem_index
problem_name=contest_info.problem_name
for i in range(len(problem_index)):
    print(problem_index[i]+' '+problem_name[i])

if(not file_management.file_exists(strings.path+str(contest_id))):
    contest_create.create_contest(contest_id)
