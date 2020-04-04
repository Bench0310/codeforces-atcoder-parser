import file_management
import prompt_handling
import string_manip
from problem_class import Problem
import strings
import website_handler
import system_action
import commands

class Contest:
    def __init__(self,path,contest_id,url):
        self.path=path+[contest_id]
        self.problems={}
        self.last_problem_index=''
        if(file_management.file_exists(string_manip.path_win(self.path))):
            metadata=file_management.read_file(string_manip.path_win(self.path+['metadata.txt']))
            problem_info=metadata.split('\n')
            for p in problem_info:
                problem_index,problem_name,test_cnt=p.split('|')
                if(self.last_problem_index==''):
                    self.last_problem_index=problem_index.lower()
                problem_path=self.path+[contest_id+problem_index+' '+problem_name]
                self.problems[problem_index.lower()]=Problem(problem_path,contest_id,problem_index,problem_name,int(test_cnt),True)
        else:
            file_management.create_folder(string_manip.path_win(self.path))
            contest_data_source=website_handler.get_source(url)
            source_index=contest_data_source.find(strings.problem_one)
            while(source_index!=-1):
                quotation_index_left=contest_data_source.find(strings.problem_index_left,source_index)+len(strings.problem_index_left)
                quotation_index_right=contest_data_source.find(strings.problem_index_right,quotation_index_left)
                problem_index=contest_data_source[quotation_index_left:quotation_index_right]
                if(self.last_problem_index==''):
                    self.last_problem_index=problem_index.lower()
                name_index_left=contest_data_source.find(strings.problem_name_left,quotation_index_right)+len(strings.problem_name_left)+len(problem_index)+2
                name_index_right=contest_data_source.find(strings.problem_name_right,name_index_left)
                problem_name_temp=contest_data_source[name_index_left:name_index_right]
                problem_name=''
                for c in problem_name_temp:
                    if(c in strings.allowed_chars):
                        problem_name+=c
                if(problem_name==''): problem_name='noname'
                file_management.create_folder(string_manip.path_win(self.path+[contest_id+problem_index+' '+problem_name]))
                self.problems[problem_index.lower()]=Problem(self.path+[contest_id+problem_index+' '+problem_name],contest_id,problem_index,problem_name,0,False)
                test_index=source_index
                next_source_index=contest_data_source.find(strings.problem_one,source_index+1)
                while(test_index<next_source_index or (next_source_index==-1 and test_index!=-1)):
                    test_index_left=contest_data_source.find(strings.test_left,test_index)+len(strings.test_left)
                    test_index_right=contest_data_source.find(strings.test_right,test_index_left)
                    test_in_string=contest_data_source[test_index_left:test_index_right]
                    test_in=string_manip.beautify_test(test_in_string)
                    test_index_left=contest_data_source.find(strings.test_left,test_index_right)+len(strings.test_left)
                    test_index_right=contest_data_source.find(strings.test_right,test_index_left)
                    test_out_string=contest_data_source[test_index_left:test_index_right]
                    test_out=string_manip.beautify_test(test_out_string)
                    self.problems[problem_index.lower()].add_test(test_in,test_out)
                    test_index=contest_data_source.find(strings.test_left,test_index_right)
                source_index=next_source_index
        if(len(self.problems)>0):
            self.make_metadata()
        else:
            file_management.delete_empty_folder(string_manip.path_win(self.path))
    def make_metadata(self):
        metadata=''
        for p in self.problems.values():
            metadata+=p.problem_index+'|'+p.problem_name+'|'+str(p.test_cnt)+'\n'
        file_management.create_file_win(string_manip.path_win(self.path+['metadata.txt']),metadata[:-1])
    def solve(self):
        args=list(filter(None,input().lower().split(' ')))
        if(len(args)==0):
            args.append('')
        if(args[0] in self.problems):
            args=['run']+args
        command=args[0]
        args_num=len(args)-1
        found=False
        parsed=False
        for comm in commands.commands:
            if(comm.name==command):
                found=True
                parsed=comm.parse(self,args[1:])
        if(not found):
            prompt_handling.prompt_invalid_command(command)
        elif(not parsed):
            return 1
        elif(command=='run'):
            self.problems[args[1]].run()
        elif(command=='code'):
            self.problems[args[1]].open_cpp(args[2])
        elif(command=='codeall'):
            for p in self.problems.values():
                p.open_cpp(strings.tp_main)
            for p in reversed(self.problems.values()):
                p.open_cpp(strings.tp_main)
        elif(command=='debug'):
            self.problems[args[1]].open_cbp(args[2])
        elif(command=='debugall'):
            for p in self.problems.values():
                p.open_cbp(strings.tp_main)
        elif(command=='io'):
            self.problems[args[1]].print_io()
        elif(command=='add'):
            self.problems[args[1]].add_test_manually()
            self.make_metadata()
        elif(command=='keep'):
            self.problems[args[1]].rm_test_keep(int(args[2]))
            self.make_metadata()
        elif(command=='rm'):
            self.problems[args[1]].rm_test_rm(int(args[2]))
            self.make_metadata()
        elif(command=='tl'):
            self.problems[args[1]].set_time_limit(int(args[2]))
        elif(command=='stress'):
            self.problems[args[1]].stress(int(args[2]))
            self.make_metadata()
        elif(command=='check'):
            self.problems[args[1]].check(int(args[2]))
            self.make_metadata()
        elif(command=='path'):
            self.problems[self.last_problem_index].copy_path()
        elif(command=='pathx'):
            self.problems[args[1]].copy_path()
        elif(command=='cls'):
            system_action.clear_screen()
        elif(command=='help'):
            prompt_handling.prompt_help(strings.help_problem)
        elif(command=='exit'):
            return 0
        return 1
