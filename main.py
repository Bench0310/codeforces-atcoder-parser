import input_output
import contest_info
import website_source

contest_id=input_output.get_contest()
if(not contest_info.contest_exists(contest_id)):
    input_output.message_contest_does_not_exist()
    exit()

contest_info.get_problems(contest_id)
problem_index=contest_info.problem_index
problem_name=contest_info.problem_name
for i in range(len(problem_index)):
    print(problem_index[i]+' '+problem_name[i])
