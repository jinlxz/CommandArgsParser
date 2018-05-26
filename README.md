# CommandArgsParser
this project provide a code template for parsing command line arguments, it eases the process to create a python command line application, developer can create a python application with complex and flexible command line arguments rapidly and focus on the coding of business logic.

## 1. usage
### 1.1 adding user-defined options <a name="section_1_1"></a>
download this project, use the script cmd_arg_parser.py as a base and add some arguments used in your application to the cmd_args_map dictionary in the cmd_arg_parse class in the sript, this dictionary represents all valid command line options, developer can add user-defined options here to add the options to the application.\
adding a switch-styled option refer to the following format.
```
    <option_name_cmd>:(self.process_bool_option,"<option_name_internal>")
```  
adding a option of key-value pair refer to the following format.
```
    <option_name_cmd>:(self.process_keyvalue_option,"<option_name_internal>")
```        
option_name_cmd is the name of the option used in command line, type string.\
option_name_internal is the name of the option as a key to stored in the self.real_cmd_options dictionary, type string. 
### 1.2 using the cmd_arg_parser module in your project.
import the cmd_arg_parser module in your project and add the following code in your main function to parse the command line arguments.
```
    cmd_parser=cmd_arg_parser.cmd_arg_parser(sys.argv)
    cmd_parser.parse_cmd_args()
    # all command line options and argumetns are stored 
    # in cmd_parser.real_cmd_options dictionary. 
    # do some business logic based on the options stored in the 
    # md_parser.real_cmd_options dictionary.
```
the cmd_parser.real_cmd_options dictionary field is used to store all command line options and arguments after parsing the command line string successfully, it stores switch-styled options, key-value pair options, list of positional arguments.
you can refer to all the command line options by referring to this variable as follows:
```
    cmd_parser.real_cmd_options[option1]  
    cmd_parser.real_cmd_options["position_arg_list"]
```  
the option1 key is defined by developers in self.cmd_args_list, refer to self.cmd_args_list in [section 1.1](#section_1_1) for more information.
the value for position_arg_list key is a list of all positional arguments.
switch-styled options have the value True or False.  

developers can focus on the coding of business logic based on the content of cmd_parser.real_cmd_options dictionary. 