'''
Created on Sep 18, 2021

@author: mballance
'''
import configparser
import os

import jinja2
import yaml

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

    @classmethod
    def mk(cls, tmpl_id, vte_file):
        fp = open(vte_file, "r")

        # Determine whether this is an old-style 
        # config file or a new-style YAML file
        # - If we encounter '[' first, then it's a config file
        # - If we encounter ':' first, then it's a YAML file
        is_config = False
        is_yaml = False

        while True:
            c = fp.read(1)

            if c == -1:
                break
            elif c == '#':
                # Comment to end of line
                while True:
                    c = fp.read(1)
                    if c == '\n' or c == -1:
                        break
            elif c == '[':
                is_config = True
                break
            elif c == ':':
                is_yaml = True
                break

            if is_config or is_yaml:
                break

        fp.seek(0)

        ret = None
        if is_config:
            ret = cls._mk_config(tmpl_id, fp, vte_file)
        elif is_yaml:
            ret = cls._mk_yaml(tmpl_id, fp, vte_file)
        else:
            raise Exception("Cannot determine type of file %s" % vte_file)
        
        fp.close()

        return ret

    @classmethod
    def _mk_config(cls, tmpl_id, fp, vte_file):
        tmpl_dir = os.path.dirname(vte_file)

        vte = configparser.ConfigParser()
        vte.read(fp)
        
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

    @classmethod
    def _mk_yaml(cls, tmpl_id, fp, vte_file):
        tmpl_dir = os.path.dirname(vte_file)

        doc = yaml.load(fp, Loader=yaml.FullLoader)

        ret = TemplateInfo(tmpl_id, tmpl_dir)

        if "template" not in doc.keys():
            raise Exception("Missing root 'template' section in %s" % vte_file)
        template = doc["template"]

        if "description" not in template.keys():
            raise Exception("No descrption in template-descriptor %s" % vte_file)
        ret.desc = template["description"].strip()

        if "parameters" in template.keys():
            for p in template["parameters"]:
                if "name" not in p.keys():
                    raise Exception("Missing parameter name")
                if "description" in p.keys():
                    desc = p["description"].strip()
                else:
                    desc = ""
                if "default" in p.keys():
                    default_val = p["default"].strip()
                    has_default = True
                else:
                    default_val = ""
                    has_default = False
                
                param = Parameter(p["name"], desc, has_default, default_val)
                ret.parameters[p["name"]] = param

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
