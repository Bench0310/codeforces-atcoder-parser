import strings
import prompt_handling
import commands

class ArgumentInt:
    def __init__(self,name,opt_range):
        self.name=name
        self.opt_range=opt_range
    def parse(self,arg):
        if(not (arg.isdigit() or (arg[0]=='-' and arg[1:].isdigit()))):
            prompt_handling.prompt_not_an_int(self.name,arg)
            return False
        if(self.opt_range!=None and (not (self.opt_range[0]<=int(arg) and int(arg)<=self.opt_range[1]))):
            prompt_handling.prompt_int_not_in_range(self.name,arg,self.opt_range)
            return False
        return True

class ArgumentStr:
    def __init__(self,name,options,forbidden):
        self.name=name
        self.options=options
        self.forbidden=forbidden
    def parse(self,arg):
        if(self.options!=None and (not arg in self.options)):
            prompt_handling.prompt_str_not_in_options(self.name,arg,self.options)
            return False
        if(self.forbidden!=None and arg in self.forbidden):
            prompt_handling.prompt_str_in_forbidden(self.name,arg)
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
