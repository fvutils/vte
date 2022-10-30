
import os
import jinja2
import stat
from vte.template_rgy import TemplateRgy

class CmdGenerate(object):

    def __call__(self, args):
        parameters = args.parameters
        rgy = TemplateRgy.inst()

        rgy.find_templates()

        if args.template not in rgy.template_map.keys():
            raise Exception("template %s does not exist" % args.template)

        template = rgy.template_map[args.template]
    
        env = jinja2.Environment(
                loader=template,
                extensions=['jinja2_strcase.StrcaseExtension'])
    
        global_vars = {
            "name" : args.name
        }
    
        # First, check all template parameters
        # and set the default or take user value
        for param_k in template.parameters.keys():
            param = template.parameters[param_k]
       
            if param_k in parameters.keys():
                global_vars[param_k] = parameters[param_k]
            elif param.has_default == True:
                global_vars[param_k] = param.default
            else:
               raise Exception("Parameter \"" + param_k + "\" is not specified")
        
            for param_k in parameters.keys():
                if param_k not in template.parameters.keys():
                    print("Warning: user-specified parameter \"" + param_k + "\" has no effect")

        # If 'force' is not set, check for files that might be overwritten
        existing_files = False
   
        if args.force == False:
            for tmpl in env.list_templates():
                tmpl_e = env.get_template(tmpl)

                # Provide global variables to the template to enable
                # expansion when querying the module (below)
                tmpl_e.globals = global_vars
       
                filename = self.substitute(global_vars, tmpl_e.name)
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
        
                filename = self.substitute(global_vars, filename)
            
                if os.path.exists(filename):
                    print("Error: output file \"" + filename + "\" already exists")
                    existing_files = True

        if existing_files == True:
            raise Exception("Existing files")
        
        for tmpl in env.list_templates():
            tmpl_e = env.get_template(tmpl)
       
            filename = self.substitute(global_vars, tmpl_e.name)
            file_dir = os.path.dirname(filename)
            try:
                filename = tmpl_e.module.filename
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
        
            filename = self.substitute(global_vars, filename)

            print("Note: processing template %s => %s" % (tmpl_e.name, filename))
            result = tmpl_e.render(global_vars)

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

    def substitute(self, vars, str):
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
      
        return str
