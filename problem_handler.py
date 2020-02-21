import path_maker
import file_management
import code_maker
import system_action
import prompt_handling
import runner

class Problem:
    #init
    def __init__(self,contest_id,problem_index,problem_name,path):
        self.contest_id=contest_id
        self.problem_index=problem_index
        self.problem_name=problem_name
        self.sample_test_num=0
        self.sample_test_in=[]
        self.sample_test_out=[]
        self.tl=10
        self.path=path_maker.path_self(self,path)
        file_management.create_folder(self.path)
        file_management.create_folder(path_maker.path_problem(self))
        for tp in ['main','bf','gen']:
            file_management.create_file(path_maker.path_problem_cpp(self,tp),code_maker.code_cpp())
            file_management.create_file(path_maker.path_problem_cbp(self,tp),code_maker.code_cbp(self,tp))
        file_management.create_folder(path_maker.path_io(self))
        file_management.create_folder(path_maker.path_checker(self))
        for tp in ['main','bf','gen']:
            file_management.create_file(path_maker.path_checker_compile(self,tp),code_maker.code_cmd_compile(self,tp))
        file_management.create_file(path_maker.path_checker_run(self,'bf'),code_maker.code_cmd_bf(self))
        file_management.create_file(path_maker.path_checker_run(self,'gen'),code_maker.code_cmd_gen(self))
        file_management.create_file(path_maker.path_checker_stressin(self),'')
        file_management.create_file(path_maker.path_checker_stressout(self),'')
        file_management.create_file(path_maker.path_checker_stresstest(self),code_maker.code_cmd_stresstest(self))
        file_management.create_folder(path_maker.path_temp(self))
        file_management.create_file(path_maker.path_temp_problemindex(self),self.problem_index)
        file_management.create_file(path_maker.path_temp_problemname(self),self.problem_name)
        file_management.create_file(path_maker.path_temp_sampletestnum(self),str(self.sample_test_num))
        for tp in ['main','bf','gen']:
            file_management.create_file(path_maker.path_temp_cppopener(self,tp),code_maker.code_cpp_opener(self,tp))
            file_management.create_file(path_maker.path_temp_cbpopener(self,tp),code_maker.code_cbp_opener(self,tp))
    #test_cases
    def add_sample_test(self,sample_in,sample_out):
        self.sample_test_num+=1
        self.sample_test_in.append(sample_in)
        self.sample_test_out.append(sample_out)
        file_management.create_file(path_maker.path_io_in(self,self.sample_test_num),self.sample_test_in[-1])
        file_management.create_file(path_maker.path_io_out(self,self.sample_test_num),self.sample_test_out[-1])
        file_management.create_file(path_maker.path_checker_test(self,self.sample_test_num),code_maker.code_cmd_test(self,self.sample_test_num))
        file_management.create_file(path_maker.path_temp_sampletestnum(self),str(self.sample_test_num))
    #checker
    def checker(self):
        system_action.run_batch(path_maker.path_checker_compile(self,'main'))
        for j in range(self.sample_test_num):
            prompt_handling.prompt_test(j+1)
            verdict=runner.get_verdict(self,'main',j+1)
            if(verdict=='TLE'):
                prompt_handling.prompt_test_status('TLE')
            elif(verdict=='OK'):
                prompt_handling.prompt_test_status('OK')
            elif(verdict=='WA'):
                sample_test_output=file_management.read_file(path_maker.path_checker_output(self,j+1))
                sample_test_answer=self.sample_test_out[j]
                prompt_handling.prompt_test_status('WA')
                prompt_handling.prompt_output_comparison(sample_test_output,sample_test_answer)
        prompt_handling.prompt_newline(2)
    #stress
    def stress(self,num):
        for tp in ['main','bf','gen']:
            system_action.run_batch(path_maker.path_checker_compile(self,tp))
        for j in range(num):
            prompt_handling.prompt_stress(j+1)
            if(runner.get_verdict(self,'gen')=='TLE'):
                prompt_handling.prompt_tle('gen')
                break
            if(runner.get_verdict(self,'bf')=='TLE'):
                prompt_handling.prompt_tle('bf')
                break
            verdict=runner.get_verdict(self,'main')
            if(verdict=='TLE'):
                prompt_handling.prompt_test_status('TLE')
                break
            elif(verdict=='OK'):
                prompt_handling.prompt_test_status('OK')
            elif(verdict=='WA'):
                sample_test_input=file_management.read_file(path_maker.path_checker_stressin(self))
                sample_test_output=file_management.read_file(path_maker.path_checker_stressoutput(self))
                sample_test_answer=file_management.read_file(path_maker.path_checker_stressout(self))
                prompt_handling.prompt_test_status('WA')
                prompt_handling.prompt_input_output_comparison(sample_test_input,sample_test_output,sample_test_answer)
                self.add_sample_test(sample_test_input,sample_test_answer)
                break
