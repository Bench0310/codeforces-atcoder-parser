import file_management
import prompt_handling
import string_manip
from problem_class import Problem
import strings
import website_handler
import system_action
import commands
import code_maker

class Contest:
    def __init__(self,path,contest_id,url,platform,path_offline,path_templates):
        self.path=path+[contest_id]
        self.platform=platform
        self.problems={}
        self.last_problem_index=''
        self.path_templates=path_templates
        if(file_management.file_exists(self.path)):
            metadata=file_management.read_file(self.path+['metadata.txt'])
            problem_info=metadata.split('\n')
            for p in problem_info:
                problem_index,problem_name,test_cnt=p.split('|')
                if(self.last_problem_index==''):
                    self.last_problem_index=problem_index.lower()
                problem_path=self.path+[contest_id+problem_index+' '+problem_name]
                self.problems[problem_index.lower()]=Problem(problem_path,contest_id,problem_index,problem_name,int(test_cnt),True)
        elif(platform==strings.pl_cf):
            file_management.create_folder(self.path)
            contest_data_source=(website_handler.get_source(url,strings.pl_cf) if path_offline==None else file_management.read_file(path_offline))
            source_index=contest_data_source.find(strings.problem_one_cf)
            while(source_index!=-1):
                quotation_index_left=contest_data_source.find(strings.problem_index_left_cf,source_index)+len(strings.problem_index_left_cf)
                quotation_index_right=contest_data_source.find(strings.problem_index_right_cf,quotation_index_left)
                problem_index=contest_data_source[quotation_index_left:quotation_index_right]
                if(self.last_problem_index==''):
                    self.last_problem_index=problem_index.lower()
                name_index_left=contest_data_source.find(strings.problem_name_left_cf,quotation_index_right)+len(strings.problem_name_left_cf)+len(problem_index)+2
                name_index_right=contest_data_source.find(strings.problem_name_right_cf,name_index_left)
                problem_name_temp=contest_data_source[name_index_left:name_index_right]
                problem_name=''
                for c in problem_name_temp:
                    if(c in strings.allowed_chars):
                        problem_name+=c
                if(problem_name=='' or problem_name.isspace()): problem_name='noname'
                problem_name=' '.join(problem_name.split())
                file_management.create_folder(self.path+[contest_id+problem_index+' '+problem_name])
                self.problems[problem_index.lower()]=Problem(self.path+[contest_id+problem_index+' '+problem_name],contest_id,problem_index,problem_name,0,False)
                test_index=contest_data_source.find(strings.test_left_cf,source_index)
                next_source_index=contest_data_source.find(strings.problem_one_cf,source_index+1)
                while(test_index!=-1 and (test_index<next_source_index or next_source_index==-1)):
                    test_index_left=contest_data_source.find(strings.test_left_cf,test_index)+len(strings.test_left_cf)
                    test_index_right=contest_data_source.find(strings.test_right_cf,test_index_left)
                    test_in_tmp_string=contest_data_source[test_index_left:test_index_right]
                    test_in_string=''
                    if(test_in_tmp_string.find(strings.sample_test_left_one_cf)==-1):
                        test_in_string=test_in_tmp_string
                    else:
                        tmp_index=test_in_tmp_string.find(strings.sample_test_left_one_cf)
                        while(tmp_index!=-1):
                            tmp_index_left=test_in_tmp_string.find(strings.sample_test_left_two_cf,tmp_index)+len(strings.sample_test_left_two_cf)
                            tmp_index_right=test_in_tmp_string.find(strings.sample_test_right_cf,tmp_index_left)
                            test_in_string+=test_in_tmp_string[tmp_index_left:tmp_index_right]+'\n'
                            tmp_index=test_in_tmp_string.find(strings.sample_test_left_one_cf,tmp_index_right)
                    test_in=string_manip.beautify_test(test_in_string)
                    test_index_left=contest_data_source.find(strings.test_left_cf,test_index_right)+len(strings.test_left_cf)
                    test_index_right=contest_data_source.find(strings.test_right_cf,test_index_left)
                    test_out_string=contest_data_source[test_index_left:test_index_right]
                    test_out=string_manip.beautify_test(test_out_string)
                    self.problems[problem_index.lower()].add_test(test_in,test_out)
                    test_index=contest_data_source.find(strings.test_left_cf,test_index_right)
                source_index=next_source_index
        elif(platform==strings.pl_atc):
            file_management.create_folder(self.path)
            contest_data_source=(website_handler.get_source(url,strings.pl_atc) if path_offline==None else file_management.read_file(path_offline))
            source_index=contest_data_source.find(strings.problem_one_atc)
            while(source_index!=-1):
                quotation_index_left=source_index+len(strings.problem_one_atc)
                quotation_index_right=contest_data_source.find(strings.problem_index_right_atc,quotation_index_left)
                problem_index=contest_data_source[quotation_index_left:quotation_index_right]
                if(self.last_problem_index==''):
                    self.last_problem_index=problem_index.lower()
                name_index_left=quotation_index_right+len(strings.problem_index_right_atc)
                name_index_right=contest_data_source.find(strings.problem_name_right_atc,name_index_left)
                problem_name_temp=contest_data_source[name_index_left:name_index_right]
                problem_name=''
                for c in problem_name_temp:
                    if(c in strings.allowed_chars):
                        problem_name+=c
                if(problem_name=='' or problem_name.isspace()): problem_name='noname'
                problem_name=' '.join(problem_name.split())
                file_management.create_folder(self.path+[contest_id+problem_index+' '+problem_name])
                self.problems[problem_index.lower()]=Problem(self.path+[contest_id+problem_index+' '+problem_name],contest_id,problem_index,problem_name,0,False)
                test_index=contest_data_source.find(strings.test_left_atc,source_index)
                next_source_index=contest_data_source.find(strings.problem_one_atc,source_index+1)
                while(test_index!=-1 and (test_index<next_source_index or next_source_index==-1)):
                    test_index_left=contest_data_source.find(strings.test_left_atc,test_index)+len(strings.test_left_atc)
                    test_index_right=contest_data_source.find(strings.test_right_atc,test_index_left)
                    test_in_string=contest_data_source[test_index_left:test_index_right]
                    test_in=string_manip.beautify_test(test_in_string)
                    test_index_left=contest_data_source.find(strings.test_left_atc,test_index_right)+len(strings.test_left_atc)
                    test_index_right=contest_data_source.find(strings.test_right_atc,test_index_left)
                    test_out_string=contest_data_source[test_index_left:test_index_right]
                    test_out=string_manip.beautify_test(test_out_string)
                    self.problems[problem_index.lower()].add_test(test_in,test_out)
                    test_index=contest_data_source.find(strings.test_left_atc,test_index_right)
                for i in range(self.problems[problem_index.lower()].test_cnt//2,0,-1):
                    self.problems[problem_index.lower()].rm_last_test()
                source_index=next_source_index
        if(len(self.problems)>0):
            self.make_metadata()
        else:
            file_management.delete_empty_folder(self.path)
    def make_metadata(self):
        metadata=''
        for p in self.problems.values():
            metadata+=p.problem_index+'|'+p.problem_name+'|'+str(p.test_cnt)+'\n'
        file_management.create_file_win(self.path+['metadata.txt'],metadata[:-1])
    def solve(self):
        command,arg,success=prompt_handling.parse_input(strings.level_problem)
        if(success==False):
            return True
        if('id' in arg):
            self.last_problem_index=arg['id']
        if(command=='run'):
            self.problems[arg['id']].run(False)
        elif(command=='code'):
            self.problems[arg['id']].open_cpp(arg['tp'])
        elif(command=='codeall'):
            for p in self.problems.values():
                p.open_cpp(strings.tp_main)
            for p in reversed(self.problems.values()):
                p.open_cpp(strings.tp_main)
        elif(command=='debug'):
            self.problems[arg['id']].open_cbp(arg['tp'])
        elif(command=='debugall'):
            for p in self.problems.values():
                p.open_cbp(strings.tp_main)
        elif(command=='io'):
            self.problems[arg['id']].print_io()
        elif(command=='add'):
            self.problems[arg['id']].add_test_manually()
            self.make_metadata()
        elif(command=='keep'):
            self.problems[arg['id']].rm_test_keep(int(arg['num']))
            self.make_metadata()
        elif(command=='rm'):
            self.problems[arg['id']].rm_test_rm(int(arg['num']))
            self.make_metadata()
        elif(command=='tl'):
            self.problems[arg['id']].set_time_limit(int(arg['tl']))
        if(command=='runbf'):
            self.problems[arg['id']].run(True)
        elif(command=='stress'):
            self.problems[arg['id']].stress(int(arg['cnt']),False)
            self.make_metadata()
        elif(command=='check'):
            self.problems[arg['id']].check(int(arg['cnt']),False)
        elif(command=='regen'):
            if(arg['rgtp']==strings.tp_bf):
                self.problems[arg['id']].stress(1,True)
            elif(arg['rgtp']==strings.tp_ch):
                self.problems[arg['id']].check(1,True)
        elif(command=='path'):
            if(self.platform==strings.pl_cf):
                self.problems[self.last_problem_index].copy_path()
            elif(self.platform==strings.pl_atc):
                self.problems[self.last_problem_index].copy_main()
        elif(command=='pathx'):
            if(self.platform==strings.pl_cf):
                self.problems[arg['id']].copy_path()
            elif(self.platform==strings.pl_atc):
                self.problems[arg['id']].copy_main()
        elif(command=='dbg'):
            compile_command,gdb_command=code_maker.code_dbg(self.problems[arg['id']],arg['tp'])
            system_action.run_command(compile_command)
            system_action.run_command(gdb_command)
        elif(command=='tm'):
            system_action.copy_to_clipboard(file_management.read_file(self.path_templates+[arg['tm']+'.h']))
        elif(command=='cls'):
            system_action.clear_screen()
        elif(command=='help'):
            prompt_handling.prompt_help(strings.level_problem)
        elif(command=='exit'):
            return False
        return True
