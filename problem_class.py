import file_management
import path_maker
import string_manip
import strings
import code_maker

class Problem:
    def __init__(self,path,contest_id,problem_index,problem_name):
        self.path=path
        self.contest_id=contest_id
        self.problem_index=problem_index
        self.problem_name=problem_name
        #Problem
        file_management.create_folder(string_manip.path_win(path_maker.path_problem(self)))
        for tp in strings.tps:
            file_management.create_file_win(string_manip.path_win(path_maker.path_problem_cpp(self,tp)),code_maker.code_cpp())
            file_management.create_file_win(string_manip.path_win(path_maker.path_problem_cbp(self,tp)),code_maker.code_cbp(self,tp))
        #IO
        file_management.create_folder(string_manip.path_win(path_maker.path_io(self)))
        #Utils
        file_management.create_folder(string_manip.path_win(path_maker.path_utils(self)))
        file_management.create_file_wsl(string_manip.path_win(path_maker.path_utils_run(self)),code_maker.code_run(self))
        file_management.create_file_wsl(string_manip.path_win(path_maker.path_utils_stress(self)),'')
        file_management.create_file_wsl(string_manip.path_win(path_maker.path_utils_check(self)),'')
        file_management.create_file_win(string_manip.path_win(path_maker.path_utils_verdict(self)),'')
