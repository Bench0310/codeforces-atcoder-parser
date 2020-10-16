import strings

#Problem
def name_problem(self):
    return 'Code'

def name_problem_cpp(self,tp):
    if(tp==strings.tp_main): return self.contest_id+self.problem_index+' '+self.problem_name+'.cpp'
    else: return self.contest_id+self.problem_index+'_'+tp+'.cpp'

def name_problem_cbp(self,tp):
    if(tp==strings.tp_main): return self.contest_id+self.problem_index+' '+self.problem_name+'.cbp'
    else: return self.contest_id+self.problem_index+'_'+tp+'.cbp'

def name_problem_exe(self,tp):
    if(tp==strings.tp_main): return self.contest_id+self.problem_index+' '+self.problem_name
    else: return self.contest_id+self.problem_index+'_'+tp

def name_problem_dbg(self,tp):
    if(tp==strings.tp_main): return self.contest_id+self.problem_index+' '+self.problem_name+'_dbg'+'.exe'
    else: return self.contest_id+self.problem_index+tp+'_dbg'+'.exe'

#IO
def name_io(self):
    return 'IO'

def name_io_in(self,j):
    return self.problem_index+'_'+str(j)+'.in'

def name_io_out(self,j):
    return self.problem_index+'_'+str(j)+'.out'

def name_io_txt(self,tp):
    return '_'+tp+'.txt'

#Utils
def name_utils(self):
    return 'Utils'

def name_utils_run(self):
    return 'run.sh'

def name_utils_stress(self):
    return 'stress.sh'

def name_utils_check(self):
    return 'check.sh'

def name_utils_verdict(self):
    return 'verdict.txt'

def name_utils_err(self,tp):
    return '_err_'+tp+'.txt'
