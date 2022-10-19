"""Extends the Problem class with path generation."""

import name_maker

#Problem
def path_problem(self):
    """Creates the problem folder path."""
    return self.path+[name_maker.name_problem(self)]

def path_problem_cpp(self, tp):
    """Creates the C++ file path."""
    return path_problem(self)+[name_maker.name_problem_cpp(self, tp)]

def path_problem_cbp(self, tp):
    """Creates the CBP file path."""
    return path_problem(self)+[name_maker.name_problem_cbp(self, tp)]

def path_problem_exe(self, tp):
    """Creates the built exe file path."""
    return path_problem(self)+[name_maker.name_problem_exe(self, tp)]

def path_problem_dbg(self, tp):
    """Creates the debug exe file path."""
    return path_problem(self)+[name_maker.name_problem_dbg(self, tp)]

#IO
def path_io(self):
    """Creates the IO folder path."""
    return self.path+[name_maker.name_io(self)]

def path_io_in(self, j):
    """Creates the input file path."""
    return path_io(self)+[name_maker.name_io_in(self, j)]

def path_io_out(self, j):
    """Creates the output file path."""
    return path_io(self)+[name_maker.name_io_out(self, j)]

def path_io_txt(self, tp):
    """Creates the temporary text files path."""
    return path_io(self)+[name_maker.name_io_txt(self, tp)]

#Utils
def path_utils(self):
    """Creates the utils folder path."""
    return self.path+[name_maker.name_utils(self)]

def path_utils_run(self):
    """Creates the run script path."""
    return path_utils(self)+[name_maker.name_utils_run(self)]

def path_utils_stress(self):
    """Creates the stress script path."""
    return path_utils(self)+[name_maker.name_utils_stress(self)]

def path_utils_check(self):
    """Creates the check script path."""
    return path_utils(self)+[name_maker.name_utils_check(self)]

def path_utils_verdict(self):
    """Creates the verdict file path."""
    return path_utils(self)+[name_maker.name_utils_verdict(self)]

def path_utils_err(self, tp):
    """Creates the error file path."""
    return path_utils(self)+[name_maker.name_utils_err(self, tp)]
