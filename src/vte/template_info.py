'''
Created on Sep 18, 2021

@author: mballance
'''
import configparser
import os

import jinja2

class Parameter:
    def __init__(self, pname, desc, has_default, default):
        self.pname = pname
        self.desc = desc
        self.has_default = has_default
        self.default = default

class TemplateInfo (jinja2.BaseLoader):
    def __init__(self, tmpl_id, tmpl_dir):
        self.tmpl_id = tmpl_id
        self.tmpl_dir = tmpl_dir
        self.parameters = {}
        self.desc = ""

    @staticmethod
    def mk(tmpl_id, vte_file):
        tmpl_dir = os.path.dirname(vte_file)
        vte = configparser.ConfigParser()
        vte.read(vte_file)
        
        ret = TemplateInfo(tmpl_id, tmpl_dir)
        
        for s in vte.sections():
            s = s.strip()
            if s.startswith("parameter"):
                colon_idx = s.find(":")
                if s == -1:
                    print("Error: malformed parameter section \"" + s + "\"")
                pname = s[colon_idx+1:].strip()
               
                if "desc" in vte[s].keys():
                    desc = vte[s]["desc"]
                else:
                    desc = ""
                     
                if "default" in vte[s].keys():
                    default_val = vte[s]["default"]
                    has_default = True
                else:
                    default_val = ""
                    has_default = False
                
                param = Parameter(pname, desc, has_default, default_val)
                ret.parameters[pname] = param
            elif s == "template":
                if "desc" in vte[s].keys():
                    ret.desc = vte[s]["desc"];
            else:
                print("Warning: unhandled section \"" + s + "\" in template " + tmpl_id)
                
        return ret
            
    def list_templates(self):
        templates = []
        self.find_template_files(self.tmpl_dir, "", templates)
        
        return templates
    
    def find_template_files(self, parent_dir_abs, parent_name, templates):
        for f in os.listdir(parent_dir_abs):
            if parent_name == "":
                this_name = f;
            else:
                this_name = os.path.join(parent_name, f)
                
            if os.path.isdir(os.path.join(parent_dir_abs, f)):
                # Must recurse
                self.find_template_files(
                    os.path.join(parent_dir_abs, f),
                    this_name,
                    templates)
            elif f != ".vte" and f.endswith(".swp") == False:
                templates.append(this_name)
                
    
    def get_source(self, environment, template):
        path = os.path.join(self.tmpl_dir, template)
        if not os.path.exists(path):
            raise jinja2.TemplateNotFound(template)
        mtime = os.path.getmtime(path)
        f = open(path, "r")
        try:
            source = f.read()
        except:
            print("Error reading file \"" + path + "\"");
        f.close()
        return source, path, lambda: mtime == os.path.getmtime(path)
