from path_maker import *
from string_manip import *
import strings
from problem_class import *
import shutil
import file_management

if(file_management.file_exists('C:\\Bench\\CodeHub\\Test\\0C Parser')):
    shutil.rmtree('C:\\Bench\\CodeHub\\Test\\0C Parser')

file_management.create_folder('C:\\Bench\\CodeHub\\Test\\0C Parser')
p=Problem(['C','Bench','CodeHub','Test','0C Parser'],'0','C','Parser')
p.add_test('5\n','5\n')
p.add_test('8\n','8\n')
p.run()
p.stress(10)
p.check(10)
