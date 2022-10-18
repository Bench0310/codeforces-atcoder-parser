"""Implements the Problem class."""

import file_management
import path_maker
import name_maker
import string_manip
import strings
import code_maker
import system_action
import prompt_handling

class Problem:
    def __init__(self, path, contest_id, problem_index, problem_name, test_cnt, problem_exists):
        self.path = path
        self.contest_id = contest_id
        self.problem_index = problem_index
        self.problem_name = problem_name
        self.test_cnt = test_cnt
        self.time_limit = 1
        if not problem_exists:
            #Problem
            file_management.create_folder(path_maker.path_problem(self))
            for tp in strings.tps:
                file_management.create_file_win(path_maker.path_problem_cpp(self, tp), code_maker.code_cpp(self, tp))
                file_management.create_file_win(path_maker.path_problem_cbp(self, tp), code_maker.code_cbp(self, tp))
            #IO
            file_management.create_folder(path_maker.path_io(self))
            #Utils
            file_management.create_folder(path_maker.path_utils(self))
            file_management.create_file_wsl(path_maker.path_utils_run(self), code_maker.code_run(self))
            file_management.create_file_wsl(path_maker.path_utils_stress(self), code_maker.code_stress(self))
            file_management.create_file_wsl(path_maker.path_utils_check(self), code_maker.code_check(self))
            file_management.create_file_wsl(path_maker.path_utils_verdict(self), '')
            for tp in strings.tps:
                file_management.create_file_wsl(path_maker.path_utils_err(self, tp), '')
    def open_cpp(self, tp):
        system_action.open_file(path_maker.path_problem_cpp(self, tp))
    def print_io(self):
        for test_idx in range(1, self.test_cnt+1):
            test_in = file_management.read_file(path_maker.path_io_in(self, test_idx))
            test_out = file_management.read_file(path_maker.path_io_out(self, test_idx))
            prompt_handling.prompt_io(test_idx, test_in, test_out)
    def add_test(self, test_in, test_out):
        self.test_cnt += 1
        test_in = string_manip.beautify_test(test_in)
        test_out = string_manip.beautify_test(test_out)
        file_management.create_file_wsl(path_maker.path_io_in(self, self.test_cnt), test_in)
        file_management.create_file_wsl(path_maker.path_io_out(self, self.test_cnt), test_out)
    def add_test_manually(self):
        self.add_test('\n', '\n')
        system_action.open_file(path_maker.path_io_out(self, self.test_cnt))
        system_action.open_file(path_maker.path_io_in(self, self.test_cnt))
    def rm_last_test(self):
        if self.test_cnt > 0:
            file_management.delete_file(path_maker.path_io_in(self, self.test_cnt))
            file_management.delete_file(path_maker.path_io_out(self, self.test_cnt))
            self.test_cnt -= 1
    def rm_test_keep(self, num):
        num = max(num, -self.test_cnt)
        if num < 0:
            num += self.test_cnt
        while self.test_cnt > num:
            self.rm_last_test()
    def set_time_limit(self, time_limit):
        self.time_limit = time_limit
    def copy_path(self):
        system_action.copy_to_clipboard(string_manip.path_win(path_maker.path_problem_cpp(self, strings.tp_main)))
    def copy_main(self):
        system_action.copy_to_clipboard(file_management.read_file(path_maker.path_problem_cpp(self, strings.tp_main)))
    def run(self, runbf):
        system_action.run_bash(path_maker.path_utils_run(self), [
            string_manip.path_wsl(path_maker.path_problem(self)),
            string_manip.path_wsl(path_maker.path_io(self)),
            string_manip.path_wsl(path_maker.path_utils(self)),
            name_maker.name_problem_exe(self, (strings.tp_main if not runbf else strings.tp_bf)),
            name_maker.name_io_txt(self, (strings.tp_main if not runbf else strings.tp_bf)),
            name_maker.name_utils_err(self, (strings.tp_main if not runbf else strings.tp_bf)),
            self.problem_index, self.test_cnt, self.time_limit, ('' if not runbf else 'Bf')
        ])
    def stress(self, stress_cnt, regen):
        system_action.run_bash(path_maker.path_utils_stress(self), [
            string_manip.path_wsl(path_maker.path_problem(self)),
            string_manip.path_wsl(path_maker.path_io(self)),
            string_manip.path_wsl(path_maker.path_utils(self)),
            name_maker.name_problem_exe(self, strings.tp_main),
            name_maker.name_io_txt(self, strings.tp_main),
            name_maker.name_utils_err(self, strings.tp_main),
            name_maker.name_problem_exe(self, strings.tp_bf),
            name_maker.name_io_txt(self, strings.tp_bf),
            name_maker.name_utils_err(self, strings.tp_bf),
            name_maker.name_problem_exe(self, strings.tp_gen),
            name_maker.name_io_txt(self, strings.tp_gen),
            name_maker.name_utils_err(self, strings.tp_gen),
            stress_cnt, self.time_limit, name_maker.name_utils_verdict(self), ('' if not regen else 'Gen')
        ])
        if not file_management.read_file(path_maker.path_utils_verdict(self)) in ['', strings.verdict_ok] and not regen:
            test_in = file_management.read_file(path_maker.path_io_txt(self, strings.tp_gen))
            test_out = file_management.read_file(path_maker.path_io_txt(self, strings.tp_bf))
            self.add_test(test_in, test_out)
    def check(self, check_cnt, regen):
        system_action.run_bash(path_maker.path_utils_check(self), [
            string_manip.path_wsl(path_maker.path_problem(self)),
            string_manip.path_wsl(path_maker.path_io(self)),
            string_manip.path_wsl(path_maker.path_utils(self)),
            name_maker.name_problem_exe(self, strings.tp_main),
            name_maker.name_io_txt(self, strings.tp_main),
            name_maker.name_utils_err(self, strings.tp_main),
            name_maker.name_problem_exe(self, strings.tp_ch),
            name_maker.name_io_txt(self, strings.tp_ch),
            name_maker.name_utils_err(self, strings.tp_ch),
            name_maker.name_problem_exe(self, strings.tp_gen),
            name_maker.name_io_txt(self, strings.tp_gen),
            name_maker.name_utils_err(self, strings.tp_gen),
            check_cnt, self.time_limit, name_maker.name_utils_verdict(self), ('' if not regen else 'Gen')
        ])
