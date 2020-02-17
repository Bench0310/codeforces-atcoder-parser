from problem_handler import *

a=Problem('0','A','Test','C:\\Bench\\CodeHub\\Test')
for i in range(20):
    a.add_sample_test(str(i)+'\n',str(i*i)+'\n')

while(True):
    b=input()
    a.stress(100)
