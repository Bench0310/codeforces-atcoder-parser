import string_manip

def name_problem(self):
    return self.contest_id+self.problem_index+' '+self.problem_name

def name_problem_cpp(self,tp):
    if(tp=='main'): return self.contest_id+self.problem_index+' '+self.problem_name+'.cpp'
    else: return self.contest_id+self.problem_index+'_'+tp+'.cpp'

def name_problem_cbp(self,tp):
    if(tp=='main'): return self.contest_id+self.problem_index+' '+self.problem_name+'.cbp'
    else: return self.contest_id+self.problem_index+'_'+tp+'.cbp'

def name_io():
    return 'IO'

def name_io_in(self,j):
    return self.problem_index+'_'+string_manip.k_digit(j,2)+'.in'

def name_io_out(self,j):
    return self.problem_index+'_'+string_manip.k_digit(j,2)+'.out'

def name_checker():
    return 'Checker'

def name_checker_compile(self,tp):
    return '__'+self.problem_index+('_'+tp if tp!='main' else '')+'.cmd'

def name_checker_test(self,j):
    return '_'+self.problem_index+'_'+string_manip.k_digit(j,2)+'.cmd'

def name_checker_exe(self,tp):
    return self.problem_index+('_'+tp if tp!='main' else '')+'.exe'

def name_checker_output(self,j):
    return self.problem_index+'_'+string_manip.k_digit(j,2)+'_'+'output'+'.txt'

def name_checker_run(tp):
    return '_'+tp+'_'+'run'+'.cmd'

def name_checker_stressin():
    return 'stress_in'+'.txt'

def name_checker_stressout():
    return 'stress_out'+'.txt'

def name_checker_stressoutput():
    return 'stress_main_out'+'.txt'

def name_checker_stresstest(self):
    return '_'+self.problem_index+'_'+'stress'+'.cmd'

def name_temp():
    return 'temp'

def name_temp_cppopener(tp):
    return tp+'_openener'+'.cmd'

def name_temp_cbpopener(tp):
    return tp+'_debug_openener'+'.cmd'

def name_temp_problemindex():
    return 'problem_index'+'.txt'

def name_temp_problemname():
    return 'problem_name'+'.txt'

def name_temp_sampletestnum():
    return 'sample_test_num'+'.txt'
