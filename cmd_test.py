import sys
class cmd_arg_struct(object):
    def __init__(self):
        self.openfile=None
        self.target_arg_list=None
    def __str__(self):
        return str(self.openfile)+"\n"+str(self.target_arg_list)
class cmd_arg_parser(object):
    def __init__(self,cmd_args):
        self.index=1
        self.real_cmd_options=cmd_arg_struct()
        self.cmd_args_list=cmd_args
        self.cmd_args_map={
            "--help":self.display_help,
            "-h":self.display_help,
            "--version":self.display_version,
            "-ver":self.display_version,
            "--openfile":self.get_opefile_value,
            "--":self.process_option_separator
        }
    def get_cmd_map(self,arg):
        if self.cmd_args_map.get(arg) is not None:
            return self.cmd_args_map.get(arg)
        else:
            if arg.startswith("-"):
                print "invalid option {0}".format(arg)
                return self.display_help
            else:
                return self.get_position_arg_list
    def display_help(self):
        print "help information"
        sys.exit(0)
    def display_version(self):
        print "version 1.0"
        sys.exit(0)
    def get_opefile_value(self):
        self.index+=1
        self.real_cmd_options.openfile=self.cmd_args_list[self.index]
        self.index+=1
    def get_position_arg_list(self):
        self.real_cmd_options.target_arg_list=self.cmd_args_list[self.index:]
        self.index=len(self.cmd_args_list)
    def process_option_separator(self):
        self.index+=1
        self.get_position_arg_list()

    def parse_cmd_args(self):
        while self.index<len(self.cmd_args_list):
            p_arg = self.cmd_args_list[self.index]
            self.get_cmd_map(p_arg)()
if __name__=="__main__":
    cmd_parser=cmd_arg_parser(sys.argv)
    cmd_parser.parse_cmd_args()
    print cmd_parser.real_cmd_options