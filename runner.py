import system_action
import path_maker
import name_maker
import file_management

def get_verdict(self,tp,j=0): #'main',0 -> stresstest
    if(tp=='main'):
        if(j>0):
            if(system_action.run_batch_timeout(path_maker.path_checker_test(self,j),name_maker.name_checker_exe(self,'main'),self.tl)==False):
                return 'TLE'
            else:
                sample_test_output=file_management.read_file(path_maker.path_checker_output(self,j))
                sample_test_output=sample_test_output.replace(' \n','\n')
                file_management.create_file(path_maker.path_checker_output(self,j),sample_test_output)
                sample_test_answer=self.sample_test_out[j]
                if(sample_test_output==sample_test_answer):
                    return 'OK'
                else:
                    return 'WA'
        else:
            if(system_action.run_batch_timeout(path_maker.path_checker_stresstest(self),name_maker.name_checker_stresstest(self),self.tl)==False):
                return 'TLE'
            else:
                sample_test_output=file_management.read_file(path_maker.path_checker_stressoutput(self))
                sample_test_output=sample_test_output.replace(' \n','\n')
                file_management.create_file(path_maker.path_checker_stressoutput(self),sample_test_output)
                sample_test_answer=file_management.read_file(path_maker.path_checker_stressout(self))
                if(sample_test_output==sample_test_answer):
                    return 'OK'
                else:
                    return 'WA'
    elif(tp=='bf'):
        if(system_action.run_batch_timeout(path_maker.path_checker_run(self,'bf'),name_maker.name_checker_exe(self,'bf'),self.tl)==False):
            return 'TLE'
        else:
            sample_test_output=file_management.read_file(path_maker.path_checker_stressout(self))
            sample_test_output=sample_test_output.replace(' \n','\n')
            file_management.create_file(path_maker.path_checker_stressout(self),sample_test_output)
            return 'OK'
    elif(tp=='gen'):
        if(system_action.run_batch_timeout(path_maker.path_checker_run(self,'gen'),name_maker.name_checker_exe(self,'gen'),self.tl)==False):
            return 'TLE'
        else:
            return 'OK'
