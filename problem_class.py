import file_management
import path_maker
import string_manip
import strings
import code_maker
import system_action

class Problem:
    def __init__(self,path,contest_id,problem_index,problem_name,test_cnt,problem_exists):
        self.path=path
        self.contest_id=contest_id
        self.problem_index=problem_index
        self.problem_name=problem_name
        self.test_cnt=test_cnt
        self.time_limit=1
        if(problem_exists==False):
            #Problem
            file_management.create_folder(string_manip.path_win(path_maker.path_problem(self)))
            for tp in strings.tps:
                file_management.create_file_win(string_manip.path_win(path_maker.path_problem_cpp(self,tp)),code_maker.code_cpp(self,tp))
                file_management.create_file_win(string_manip.path_win(path_maker.path_problem_cbp(self,tp)),code_maker.code_cbp(self,tp))
            #IO
            file_management.create_folder(string_manip.path_win(path_maker.path_io(self)))
            #Utils
            file_management.create_folder(string_manip.path_win(path_maker.path_utils(self)))
            file_management.create_file_wsl(string_manip.path_win(path_maker.path_utils_run(self)),code_maker.code_run(self))
            file_management.create_file_wsl(string_manip.path_win(path_maker.path_utils_stress(self)),code_maker.code_stress(self))
            file_management.create_file_wsl(string_manip.path_win(path_maker.path_utils_check(self)),code_maker.code_check(self))
            file_management.create_file_win(string_manip.path_win(path_maker.path_utils_verdict(self)),'')
    def open_cpp(self,tp):
        system_action.open_file(string_manip.path_win_q(path_maker.path_problem_cpp(self,tp)))
    def open_cbp(self,tp):
        system_action.open_file(string_manip.path_win_q(path_maker.path_problem_cbp(self,tp)))
    def add_test(self,test_in,test_out):
        self.test_cnt+=1
        file_management.create_file_win(string_manip.path_win(path_maker.path_io_in(self,self.test_cnt)),test_in)
        file_management.create_file_win(string_manip.path_win(path_maker.path_io_out(self,self.test_cnt)),test_out)
    def add_test_manually(self):
        self.add_test('','')
        system_action.open_file(string_manip.path_win_q(path_maker.path_io_in(self,self.test_cnt)))
        system_action.open_file(string_manip.path_win_q(path_maker.path_io_out(self,self.test_cnt)))
    def rm_last_test(self):
        if(self.test_cnt>0):
            file_management.delete_file(string_manip.path_win(path_maker.path_io_in(self,self.test_cnt)))
            file_management.delete_file(string_manip.path_win(path_maker.path_io_out(self,self.test_cnt)))
            self.test_cnt-=1
    def rm_test_keep(self,num):
        while(self.test_cnt>num):
            self.rm_last_test()
    def rm_test_rm(self,num):
        cnt=min(self.test_cnt,num)
        for _ in range(cnt):
            self.rm_last_test()
    def set_time_limit(self,time_limit):
        self.time_limit=time_limit
    def copy_path(self):
        system_action.copy_to_clipboard(string_manip.path_win(path_maker.path_problem_cpp(self,strings.tp_main)))
    def run(self):
        system_action.run_bash(string_manip.path_wsl_q(path_maker.path_utils_run(self)),[self.test_cnt,self.time_limit])
    def stress(self,stress_cnt):
        system_action.run_bash(string_manip.path_wsl_q(path_maker.path_utils_stress(self)),[stress_cnt,self.time_limit])
        if(file_management.read_file(string_manip.path_win(path_maker.path_utils_verdict(self)))==strings.verdict_wa):
            test_in=file_management.file_read(string_manip.path_win(path_maker.path_io_txt(self,strings.tp_gen)))
            test_out=file_management.file_read(string_manip.path_win(path_maker.path_io_txt(self,strings.tp_bf)))
            self.add_test(test_in,test_out)
    def check(self,check_cnt):
        system_action.run_bash(string_manip.path_wsl_q(path_maker.path_utils_check(self)),[check_cnt,self.time_limit])
