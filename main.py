import input_output
import contest_info
import website_source

contest_id=input_output.get_contest()
if(contest_info.contest_exists(contest_id)==0):
    input_output.message_contest_does_not_exist()
    exit()
