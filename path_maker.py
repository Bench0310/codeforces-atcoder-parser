import name_maker

#Problem
def path_problem(self):
    return self.path+[name_maker.name_problem(self)]

def path_problem_cpp(self,tp):
    return path_problem(self)+[name_maker.name_problem_cpp(self,tp)]

def path_problem_cbp(self,tp):
    return path_problem(self)+[name_maker.name_problem_cbp(self,tp)]

def path_problem_exe(self,tp):
    return path_problem(self)+[name_maker.name_problem_exe(self,tp)]

#IO
def path_io(self):
    return self.path+[name_maker.name_io(self)]

def path_io_in(self,j):
    return path_io(self)+[name_maker.name_io_in(self,j)]

def path_io_out(self,j):
    return path_io(self)+[name_maker.name_io_out(self,j)]

def path_io_txt(self,tp):
    return path_io(self)+[name_maker.name_io_txt(self,tp)]

#Utils
def path_utils(self):
    return self.path+[name_maker.name_utils(self)]

def path_utils_run(self):
    return path_utils(self)+[name_maker.name_utils_run(self)]

def path_utils_stress(self):
    return path_utils(self)+[name_maker.name_utils_stress(self)]

def path_utils_check(self):
    return path_utils(self)+[name_maker.name_utils_check(self)]

def path_utils_verdict(self):
    return path_utils(self)+[name_maker.name_utils_verdict(self)]

def path_utils_err(self,tp):
    return path_utils(self)+[name_maker.name_utils_err(self,tp)]
