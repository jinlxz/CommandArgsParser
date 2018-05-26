import sys
class cmd_arg_parser(object):
    def __init__(self,cmd_args):
        self.index=1
        """dictionary to store all command line arguments after parsing the command line successfully.
        the dictionary stores switch-styled options, key-value pair options, list of positional arguments.
        you can refer to all the command line options by referring to this variable as follows:
            cmd_arg_parser.real_cmd_options[option1]  
            cmd_arg_parser.real_cmd_options[option2]
            cmd_arg_parser.real_cmd_options["position_arg_list"]  
        the option1,option2 keys are defined by devepers in self.cmd_args_list, refer to self.cmd_args_list for more information.
        the value for position_arg_list key is a list of all positional arguments.
        switch-styled options have the value True or False 
        """
        self.real_cmd_options={}
        #the original list of command line arguments.
        self.cmd_args_list=cmd_args
        """dictionary to represent all valid command line options, developer can add user-defined options here to add the options to the application.
        adding a switch-styled option refer to the following format.
        <option_name_cmd>:(self.process_bool_option,"<option_name_internal>")  
        adding a option of key-value pair refer to the following format.
        <option_name_cmd>:(self.process_keyvalue_option,"<option_name_internal>")        
        option_name_cmd is the name of the option used in command line, type string.
        option_name_internal is the name of the option as a key to stored in the self.real_cmd_options dictionary, type string.        
        """
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