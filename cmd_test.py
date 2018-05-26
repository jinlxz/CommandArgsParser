import sys
class cmd_arg_parser(object):
    def __init__(self,cmd_args):
        self.index=1
        self.real_cmd_options={}
        self.cmd_args_list=cmd_args
        self.cmd_args_map={
            "--help":(self.display_help,"help"),
            "-h":(self.display_help,"help"),
            "--version":(self.display_version,"version"),
            "-ver":(self.display_version,"version"),
            "--openfile":(self.process_keyvalue_option,"openfile"),
            "--enable-smp":(self.process_bool_option,"enable-smp"),
            "--":(self.process_option_separator,"separator")
        }
    def get_cmd_function(self,arg):
        if self.cmd_args_map.get(arg) is not None:
            return self.cmd_args_map.get(arg)
        else:
            if arg.startswith("-"):
                print "invalid option {0}".format(arg)
                return (self.display_help,"help")
            else:
                return (self.get_position_arg_list,"position_arg_list")
    def process_bool_option(self,name):
        self.real_cmd_options[name]=True;
        self.index+=1
    def process_keyvalue_option(self,name):
        self.index+=1
        self.real_cmd_options[name]=self.cmd_args_list[self.index]
        self.index+=1
    def display_help(self,name):
        print "help information"
        sys.exit(0)
    def display_version(self,name):
        print "version 1.0"
        sys.exit(0)
    def get_position_arg_list(self,name):
        self.real_cmd_options[name]=self.cmd_args_list[self.index:]
        self.index=len(self.cmd_args_list)
    def process_option_separator(self,name):
        self.index+=1
        self.get_position_arg_list(name)

    def parse_cmd_args(self):
        while self.index<len(self.cmd_args_list):
            p_arg = self.cmd_args_list[self.index]
            arg_process_func,arg_name=self.get_cmd_function(p_arg)
            arg_process_func(arg_name)
if __name__=="__main__":
    cmd_parser=cmd_arg_parser(sys.argv)
    cmd_parser.parse_cmd_args()
    print cmd_parser.real_cmd_options