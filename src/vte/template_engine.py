import os
import stat

import jinja2

from vte import substitute
from vte.template_rgy import TemplateInfo


class TemplateEngine:

    # template: TemplateInfo
    def __init__(self, template : TemplateInfo, outdir=None):
        self.outdir = outdir
        self.template = template
        self.force = False
#        templLoader = FileSystemLoader();
#        self.env = Environment(loader=templLoader)
       
    def generate(self, name, parameters):
        env = jinja2.Environment(loader=self.template)
        
    #    jinja2.Environment.globals['name'] = "foo";
        global_vars = {
            "name" : name
        }
        
        # First, check all template parameters
        # and set the default or take user value
        for param_k in self.template.parameters.keys():
            param = self.template.parameters[param_k]
           
            if param_k in parameters.keys():
                global_vars[param_k] = parameters[param_k]
            elif param.has_default == True:
                global_vars[param_k] = param.default
            else:
                print("Error: parameter \"" + param_k + "\" is not specified")
                return
            
        for param_k in parameters.keys():
            if param_k not in self.template.parameters.keys():
                print("Warning: user-specified parameter \"" + param_k + "\" has no effect")
    
        # If 'force' is not set, check for files that might be overwritten
        existing_files = False
       
        if self.force == False:
            for tmpl in env.list_templates():
                tmpl_e = env.get_template(tmpl)
           
                filename = substitute(global_vars, tmpl_e.name)
                file_dir = os.path.dirname(filename)
                try:
                    filename_u = tmpl_e.module.filename
                    
                    if filename_u.find("/") != -1:
                        # User has specified a relative path, so we assume 
                        # this is relative to the output directory
                        filename = filename_u
                    else:
                        # Just a simple filename, so we assume it is relative
                        # to the template file
                        filename = file_dir + "/" + filename_u
                except:
                    pass
            
                filename = substitute(global_vars, filename)
                
                if self.outdir is not None:
                    filename = os.path.join(self.outdir, filename)
                
                if os.path.exists(filename):
                    print("Error: output file \"" + filename + "\" already exists")
                    existing_files = True
    
        if existing_files == True:
            exit(1)
            
        for tmpl in env.list_templates():
            tmpl_e = env.get_template(tmpl)
           
            filename = substitute(global_vars, tmpl_e.name)
            file_dir = os.path.dirname(filename)
            try:
                filename = tmpl_e.module.filename;
                
                filename_u = tmpl_e.module.filename
                    
                if filename_u.find("/") != -1 or file_dir == "":
                    # User has specified a relative path, so we assume 
                    # this is relative to the output directory
                    filename = filename_u
                else:
                    # Just a simple filename, so we assume it is relative
                    # to the template file
                    filename = file_dir + "/" + filename_u
            except:
                pass
            
            filename = substitute(global_vars, filename)
            
            if self.outdir is not None:
                filename = os.path.join(self.outdir, filename)
    
            print("Note: processing template " + tmpl_e.name)        
            result = tmpl_e.render(global_vars)
    #        print("Result: " + result)
    
            file_dir = os.path.dirname(filename)
            
            if file_dir != "" and not os.path.isdir(file_dir):
                os.makedirs(file_dir)
                
            with open(filename, "w") as fh:
                fh.write(result)
            
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
