"""Implements the Argument and Command classes."""

import prompt_handling

class ArgumentNum:
    def __init__(self, name, num_range):
        self.name = name
        self.num_range = num_range
    def parse(self, arg):
        if not (arg.isdigit() or (arg[0] == '-' and arg[1:].isdigit())):
            prompt_handling.prompt_not_an_int(self.name, arg)
            return False
        if self.num_range is not None and not (self.num_range[0] <= int(arg) and int(arg) <= self.num_range[1]):
            prompt_handling.prompt_int_not_in_range(self.name, arg, self.num_range)
            return False
        return True

class ArgumentStr:
    def __init__(self, name, str_options):
        self.name = name
        self.str_options = str_options
    def parse(self, arg):
        if self.str_options is not None and arg not in self.str_options:
            prompt_handling.prompt_str_not_in_options(self.name, arg, self.str_options)
            return False
        return True

class Command:
    def __init__(self, name, arguments, description):
        self.name = name
        self.arguments = arguments
        self.description = description
    def parse(self, args):
        if len(self.arguments) != len(args):
            prompt_handling.prompt_wrong_num_of_args(self.name, len(self.arguments), len(args))
            return False
        successfully_parsed = True
        for i in range(len(args)):
            if not self.arguments[i].parse(args[i]):
                successfully_parsed = False
        return successfully_parsed
