"""Extends the Problem class with name generation for paths."""

import strings

#Problem
def name_problem(self):
    """Names the problem folder."""
    return 'Code'

def name_problem_cpp(self, tp):
    """Names the C++ file."""
    if tp == strings.tp_main: return self.contest_id+self.problem_index+' '+self.problem_name+'.cpp'
    else: return self.contest_id+self.problem_index+'_'+tp+'.cpp'

def name_problem_cbp(self, tp):
    """Names the CBP file."""
    if tp == strings.tp_main: return self.contest_id+self.problem_index+' '+self.problem_name+'.cbp'
    else: return self.contest_id+self.problem_index+'_'+tp+'.cbp'

def name_problem_exe(self, tp):
    """Names the built exe file."""
    if tp == strings.tp_main: return self.contest_id+self.problem_index+' '+self.problem_name
    else: return self.contest_id+self.problem_index+'_'+tp

def name_problem_dbg(self, tp):
    """Names the debug exe file."""
    if tp == strings.tp_main: return self.contest_id+self.problem_index+' '+self.problem_name+'_dbg'+'.exe'
    else: return self.contest_id+self.problem_index+'_'+tp+'_dbg'+'.exe'

#IO
def name_io(self):
    """Names the IO folder."""
    return 'IO'

def name_io_in(self, j):
    """Names the input file."""
    return self.problem_index+'_'+str(j)+'.in'

def name_io_out(self, j):
    """Names the output file."""
    return self.problem_index+'_'+str(j)+'.out'

def name_io_txt(self, tp):
    """Names the temporary text files."""
    return '_'+tp+'.txt'

#Utils
def name_utils(self):
    """Names the utils folder."""
    return 'Utils'

def name_utils_run(self):
    """Names the run script."""
    return 'run.sh'

def name_utils_stress(self):
    """Names the stress script."""
    return 'stress.sh'

def name_utils_check(self):
    """Names the check script."""
    return 'check.sh'

def name_utils_verdict(self):
    """Names the verdict file."""
    return 'verdict.txt'

def name_utils_err(self, tp):
    """Names the error file."""
    return '_err_'+tp+'.txt'
