import website_source
import strings

problem_source_index=[]
problem_index=[]
problem_name=[]

def contest_exists(contest_id):
    contest_list_source=website_source.get_contest_list()
    return (contest_list_source.find(strings.contest_id_one+str(contest_id))!=-1)

def get_problems(contest_id):
    contest_data_source=website_source.get_contest_data(contest_id)
    global problem_source_index
    global problem_index
    global problem_name
    source_index=contest_data_source.find(strings.problem_one)
    while(source_index!=-1):
        problem_source_index.append(source_index)
        quotation_index_left=contest_data_source.find(strings.problem_index_left,source_index)+1
        quotation_index_right=contest_data_source.find(strings.problem_index_right,quotation_index_left)
        problem_index.append(contest_data_source[quotation_index_left:quotation_index_right])
        name_index_left=contest_data_source.find(strings.problem_name_left,quotation_index_right)+19+len(problem_index[-1])+2
        name_index_right=contest_data_source.find(strings.problem_name_right,name_index_left)
        problem_name.append(contest_data_source[name_index_left:name_index_right])
        problem_name[-1]=problem_name[-1].translate({ord(c): None for c in strings.file_forbidden_chars})
        source_index=contest_data_source.find(strings.problem_one,source_index+1)
