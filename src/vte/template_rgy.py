#****************************************************************************
#* template_rgy.py
#*
#* Registry of template info discovered based on a search list
#****************************************************************************
import os

import jinja2
import configparser
#import yaml

class Parameter:
    def __init__(self, pname, desc, default):
        self.pname = pname
        self.desc = desc
        self.default = default

class TemplateInfo (jinja2.BaseLoader):
    def __init__(self, 
                 tmpl_id, 
                 vte_file):
        print("template_info::init " + tmpl_id)
        self.tmpl_id = tmpl_id
        self.tmpl_dir = os.path.dirname(vte_file)
        self.parameters = {}
       
        vte = configparser.ConfigParser()
        vte.read(vte_file)
        
        for s in vte.sections():
            print("Section: " + str(s))
            s = s.strip()
            if s.startswith("parameter"):
                colon_idx = s.find(":")
                if s == -1:
                    print("Error: malformed parameter section \"" + s + "\"")
                pname = s[colon_idx+1:].strip()
                print("  Parameter: " + pname)
                
                param = Parameter(pname, "desc", "default")
                self.parameters[pname] = param
            
    def list_templates(self):
        print("list_templates")
        templates = []
        for f in os.listdir(self.tmpl_dir):
            # TODO: must respect filter list from spec
            if f != ".vte":
                templates.append(f)
        return templates
    
    def get_source(self, environment, template):
        print("get_source")
        path = os.path.join(self.tmpl_dir, template)
        if not os.path.exists(path):
            raise jinja2.TemplateNotFound(template)
        mtime = os.path.getmtime(path)
        f = open(path, "r")
        source = f.read()
        f.close()
        print("path=" + path + " source=" + str(source))
        return source, path, lambda: mtime == os.path.getmtime(path)

        
class TemplateRgy:
    def find_templates(self, dir, template_id):
        print("find_templates ", dir)
        
        if os.path.isfile(os.path.join(dir, ".vte")):
            if len(template_id) == 0:
                print("Error: found a template marker (.vte) in a root template-path directory (" + dir + ")");
                exit(1)
            t = TemplateInfo(
                ".".join(template_id),
                os.path.join(dir, ".vte"));
            self.templates.append(t)
            self.template_map[t.tmpl_id] = t
        else:
            for d in os.listdir(dir):
                if os.path.isdir(os.path.join(dir, d)):
                    template_id.append(d)
                    self.find_templates(
                        os.path.join(dir, d),
                        template_id)
                    template_id.pop()

    def process_template(self, root_path, path):
        dflt_template_id = path[len(root_path):len(path)]
        dflt_template_id = dflt_template_id.replace('\\', '/')
        name = os.path.basename(path)
        while (len(dflt_template_id) > 0 and dflt_template_id.startswith('/')):
            dflt_template_id = dflt_template_id[1:len(dflt_template_id)]
           
        while (len(dflt_template_id) > 0 and dflt_template_id.endswith('/')):
            dflt_template_id = dflt_template_id[0:len(dflt_template_id)-1]
            
        dflt_template_id = dflt_template_id.replace('/', '.')
       
        vte_stream = file(os.path.join(path, ".vte"), "r")
        dot_vte = yaml.load(vte_stream)
        
#        tmpl = TemplateInfo(name, dflt_template_id, path)
       
#        print "Type ", type(dot_vte)
        
#        for key in dot_vte.keys():
#            print "key: ", key
             
#        print "Process template ", root_path, " ", path, " ", dflt_template_id
        
    def __init__(self, template_path):
        print("template_rgy::init ", len(template_path))
        
        self.templates = []
        self.template_map = {}
        
        for d in template_path:
            self.find_templates(d, [])
    
