import file_management
import prompt_handling
import string_manip
from problem_class import Problem
import strings
import website_handler
import argument_parser
import system_action

class Contest:
    def __init__(self,path,contest_id,url):
        self.path=path+[contest_id]
        self.problems=[]
        self.problem_indices=[]
        if(file_management.file_exists(string_manip.path_win(self.path))):
            metadata=file_management.read_file(string_manip.path_win(self.path+['metadata.txt']))
            problem_info=metadata.split('\n')
            for p in problem_info:
                problem_index,problem_name,test_cnt=p.split('|')
                problem_path=self.path+[contest_id+problem_index+' '+problem_name]
                self.problems.append(Problem(problem_path,contest_id,problem_index,problem_name,int(test_cnt),True))
                self.problem_indices.append(problem_index.lower())
        else:
            file_management.create_folder(string_manip.path_win(self.path))
            contest_data_source=website_handler.get_source(url)
            source_index=contest_data_source.find(strings.problem_one)
            while(source_index!=-1):
                quotation_index_left=contest_data_source.find(strings.problem_index_left,source_index)+len(strings.problem_index_left)
                quotation_index_right=contest_data_source.find(strings.problem_index_right,quotation_index_left)
                problem_index=contest_data_source[quotation_index_left:quotation_index_right]
                name_index_left=contest_data_source.find(strings.problem_name_left,quotation_index_right)+len(strings.problem_name_left)+len(problem_index)+2
                name_index_right=contest_data_source.find(strings.problem_name_right,name_index_left)
                problem_name_temp=contest_data_source[name_index_left:name_index_right]
                problem_name=''
                for c in problem_name_temp:
                    if(c in strings.allowed_chars):
                        problem_name+=c
                if(problem_name==''): problem_name='noname'
                file_management.create_folder(string_manip.path_win(self.path+[contest_id+problem_index+' '+problem_name]))
                self.problems.append(Problem(self.path+[contest_id+problem_index+' '+problem_name],contest_id,problem_index,problem_name,0,False))
                self.problem_indices.append(problem_index.lower())
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
                    self.problems[-1].add_test(test_in,test_out)
                    test_index=contest_data_source.find(strings.test_left,test_index_right)
                source_index=next_source_index
            self.make_metadata()
        self.last_problem_index=self.problems[0].problem_index
    def make_metadata(self):
        metadata=''
        for p in self.problems:
            metadata+=p.problem_index+'|'+p.problem_name+'|'+str(p.test_cnt)+'\n'
        file_management.create_file_win(string_manip.path_win(self.path+['metadata.txt']),metadata[:-1])
    def solve(self):
        args=list(filter(None,input().lower().split(' ')))
        command=args[0]
        args_num=len(args)-1
        if(command in self.problem_indices):
            for p in self.problems:
                if(p.problem_index.lower()==command):
                    if(args_num==0):
                        p.run()
                    else:
                        prompt_handling.prompt_wrong_num_of_args(command,0,args_num)
        elif(not command in strings.comms):
            prompt_handling.prompt_invalid_command(command)
        elif(args_num!=strings.comms_args[command]):
            prompt_handling.prompt_wrong_num_of_args(command,strings.comms_args[command],args_num)
        elif(command==strings.comm_code):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1 and argument_parser.parse_tp(args[2])==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.open_cpp(args[2])
                self.last_problem_index=args[1]
        elif(command==strings.comm_codeall):
            for p in self.problems:
                p.open_cpp(strings.tp_main)
        elif(command==strings.comm_debug):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1 and argument_parser.parse_tp(args[2])==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.open_cbp(args[2])
                self.last_problem_index=args[1]
        elif(command==strings.comm_io):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.print_io()
                self.last_problem_index=args[1]
        elif(command==strings.comm_add):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.add_test_manually()
                self.last_problem_index=args[1]
                self.make_metadata()
        elif(command==strings.comm_keep):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1 and argument_parser.parse_num(args[2])==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.rm_test_keep(int(args[2]))
                self.last_problem_index=args[1]
                self.make_metadata()
        elif(command==strings.comm_rm):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1 and argument_parser.parse_num(args[2])==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.rm_test_rm(int(args[2]))
                self.last_problem_index=args[1]
                self.make_metadata()
        elif(command==strings.comm_tl):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1 and argument_parser.parse_tl(args[2])==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.set_time_limit(int(args[2]))
                self.last_problem_index=args[1]
        elif(command==strings.comm_stress):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1 and argument_parser.parse_num(args[2])==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.stress(int(args[2]))
                self.last_problem_index=args[1]
                self.make_metadata()
        elif(command==strings.comm_check):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1 and argument_parser.parse_num(args[2])==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.check(int(args[2]))
                self.last_problem_index=args[1]
                self.make_metadata()
        elif(command==strings.comm_path):
            for p in self.problems:
                if(p.problem_index.lower()==self.last_problem_index):
                    p.copy_path()
        elif(command==strings.comm_pathx):
            if(argument_parser.parse_id(args[1],self.problem_indices)==1):
                for p in self.problems:
                    if(p.problem_index.lower()==args[1]):
                        p.copy_path()
        elif(command==strings.comm_cls):
            system_action.clear_screen()
        elif(command==strings.comm_help):
            prompt_handling.prompt_help(strings.help_problem)
        elif(command==strings.comm_exit):
            return 0
        return 1
