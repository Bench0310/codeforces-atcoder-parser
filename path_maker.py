import string_manip
import name_maker

delim='\\'

def path_self(self,path):
    return path+delim+name_maker.name_problem(self)

def path_problem(self):
    return self.path+delim+name_maker.name_problem(self)

def path_problem_cpp(self,tp):
    return path_problem(self)+delim+name_maker.name_problem_cpp(self,tp)

def path_problem_cbp(self,tp):
    return path_problem(self)+delim+name_maker.name_problem_cbp(self,tp)

def path_io(self):
    return self.path+delim+name_maker.name_io()

def path_io_in(self,j):
    return path_io(self)+delim+name_maker.name_io_in(self,j)

def path_io_out(self,j):
    return path_io(self)+delim+name_maker.name_io_out(self,j)

def path_checker(self):
    return self.path+delim+name_maker.name_checker()

def path_checker_compile(self,tp):
    return path_checker(self)+delim+name_maker.name_checker_compile(self,tp)

def path_checker_test(self,j):
    return path_checker(self)+delim+name_maker.name_checker_test(self,j)

def path_checker_exe(self,tp):
    return path_checker(self)+delim+name_maker.name_checker_exe(self,tp)

def path_checker_output(self,j):
    return path_checker(self)+delim+name_maker.name_checker_output(self,j)

def path_checker_run(self,tp):
    return path_checker(self)+delim+name_maker.name_checker_run(tp)

def path_checker_stressin(self):
    return path_checker(self)+delim+name_maker.name_checker_stressin()

def path_checker_stressout(self):
    return path_checker(self)+delim+name_maker.name_checker_stressout()

def path_checker_stressoutput(self):
    return path_checker(self)+delim+name_maker.name_checker_stressoutput()

def path_checker_stresstest(self):
    return path_checker(self)+delim+name_maker.name_checker_stresstest(self)

def path_temp(self):
    return self.path+delim+name_maker.name_temp()

def path_temp_cppopener(self,tp):
    return path_temp(self)+delim+name_maker.name_temp_cppopener(tp)

def path_temp_cbpopener(self,tp):
    return path_temp(self)+delim+name_maker.name_temp_cbpopener(tp)

def path_temp_problemindex(self):
    return path_temp(self)+delim+name_maker.name_temp_problemindex()

def path_temp_problemname(self):
    return path_temp(self)+delim+name_maker.name_temp_problemname()

def path_temp_sampletestnum(self):
    return path_temp(self)+delim+name_maker.name_temp_sampletestnum()
