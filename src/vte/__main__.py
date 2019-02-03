#****************************************************************************
#* vte main
#****************************************************************************

import argparse
import jinja2
import os
import stat
from stat import *
from . import template_rgy

def substitute(vars, str):
    i=0
    while i < len(str):
        idx = str.find("{{", i)
        
        if idx == -1:
            break
       
        end = str.find("}}", idx)
        
        if end == -1:
            print("Error: unterminated reference")
            break
        
        key = str[idx+2:end]
        
        if key in vars.keys():
            str = str[:idx] + vars[key] + str[end+2:]
            
        i=idx+2
      
    print("str: " + str) 
    return str

def generate(args, parameters, rgy):
    if args.template not in rgy.template_map.keys():
        print("Error: template does not exist")
        return

    template = rgy.template_map[args.template]
    
    env = jinja2.Environment(loader=template)
    
#    jinja2.Environment.globals['name'] = "foo";
    global_vars = {
        "name" : args.name
    }
    
    # First, check all template parameters
    # and set the default or 
    for param_k in template.parameters.keys():
        param = template.parameters[param_k]
       
        if param_k in parameters.keys():
            global_vars[param_k] = parameters[param_k]
        elif param.has_default == True:
            global_vars[param_k] = param.default
        else:
            print("Error: parameter \"" + param_k + "\" is not specified")
            return
        
    for param_k in parameters.keys():
        if param_k not in template.parameters.keys():
            print("Warning: user-specified parameter \"" + param_k + "\" has no effect")
        
    for tmpl in env.list_templates():
        tmpl_e = env.get_template(tmpl)
       
        filename = tmpl_e.name
        try:
            filename = tmpl_e.module.filename;
        except:
            pass
        
        filename = substitute(global_vars, filename)
        
        result = tmpl_e.render(global_vars)
        print("Result: " + result)
       
        dir = os.path.dirname(filename)
        
        if dir != "":
            if os.path.isdir(dir) == False:
                os.makedirs(dir)
            
        fh = open(filename, "w");
        fh.write(result)
        fh.close()
        
        chmod = ""
        try:
            chmod = tmpl_e.module.chmod
        except:
            pass
       
        chmod = chmod.strip()
        
        if chmod != "":
            mode = os.stat(filename).st_mode
            
            i=0
            is_add = True
            while i < len(chmod):
                if chmod[i] == "+":
                    is_add = True
                elif chmod[i] == "-":
                    is_add = False
                elif chmod[i] == "x":
                    if is_add:
                        mode = mode | stat.S_IEXEC
                    else:
                        mode = mode & ~stat.S_IEXEC
                elif chmod[i] == "r":
                    if is_add:
                        mode = mode | stat.S_IREAD
                    else:
                        mode = mode & ~stat.S_IREAD
                elif chmod[i] == "w":
                    if is_add:
                        mode = mode | stat.S_IWRITE
                    else:
                        mode = mode & ~stat.S_IWRITE
                else:
                    print("Error: unknown chmod character \"" + chmod[i] + "\" in chmod string \"" + chmod + "\"")
                    
                i=i+1
            os.chmod(filename, mode)
        

def main():
    parser = argparse.ArgumentParser(prog="vte")
    subparser = parser.add_subparsers(dest="subcmd")
    generate_cmd = subparser.add_parser("generate",
        help="generate source files")
    
    generate_cmd.add_argument("template", help="ID of template")
    generate_cmd.add_argument("name", help="Name to use in the template")
    generate_cmd.add_argument("parameters", 
             metavar="KEY=VALUE", 
             nargs="*",
             help="Specify other template variables")
    
    args = parser.parse_args()

    if args.name.find("=") != -1:
        print("Error: name contains '='")
        exit(1)
           
    # Check that parameters are properly-specified 
    parameters = {}
    for param in args.parameters:
        idx = param.find("=")
        if idx == -1:
            print("Error: parameter specification \"" + param + "\" doesn't contain '='");
            exit(1)
        parameters[param[:idx]] = param[idx+1:]
            
    template_path = []
    template_path.append("/project/fun/vte/vte-mballance/templates")
   
    # Bring in the template path elements from 
    if os.getenv("VTE_TEMPLATE_PATH") != None:
        for elem in os.getenv("VTE_TEMPLATE_PATH").split(":"):
            template_path.append(elem)
            
    rgy = template_rgy.TemplateRgy(template_path)
    
    if args.subcmd == "generate":
        generate(args, parameters, rgy)
    

if __name__ == "__main__":
    main()

