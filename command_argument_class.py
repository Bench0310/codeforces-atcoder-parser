import strings
import prompt_handling
import commands

class Argument:
    def __init__(self,name,ctp,num_range,str_options):
        self.name=name
        self.ctp=ctp
        self.num_range=num_range
        self.str_options=str_options
    def parse(self,arg):
        if(self.ctp==commands.arg_tp_num):
            if(not (arg.isdigit() or (arg[0]=='-' and arg[1:].isdigit()))):
                prompt_handling.prompt_not_an_int(self.name,arg)
                return False
            if(self.num_range!=0 and (not (self.num_range[0]<=int(arg) and int(arg)<=self.num_range[1]))):
                prompt_handling.prompt_int_not_in_range(self.name,arg,self.num_range)
                return False
            return True
        elif(self.ctp==commands.arg_tp_str):
            if(self.str_options!=0 and (not arg in self.str_options)):
                prompt_handling.prompt_str_not_in_options(self.name,arg,self.str_options)
                return False
            return True

class Command:
    def __init__(self,name,arguments,description):
        self.name=name
        self.arguments=arguments
        self.description=description
    def parse(self,args):
        if(len(self.arguments)!=len(args)):
            prompt_handling.prompt_wrong_num_of_args(self.name,len(self.arguments),len(args))
            return False
        successfully_parsed=True
        for i in range(len(args)):
            if(self.arguments[i].parse(args[i])==False):
                successfully_parsed=False
        return successfully_parsed
