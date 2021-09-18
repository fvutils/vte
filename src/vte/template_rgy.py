#****************************************************************************
#* template_rgy.py
#*
#* Registry of template info discovered based on a search list
#****************************************************************************
import os

from vte.template_info import TemplateInfo


class TemplateRgy:
    def find_templates(self, dir, template_id):
        
        if os.path.isfile(os.path.join(dir, ".vte")):
            if len(template_id) == 0:
                print("Error: found a template marker (.vte) in a root template-path directory (" + dir + ")");
                exit(1)
            t = TemplateInfo.mk(".".join(template_id), os.path.join(dir, ".vte"));
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

    def __init__(self, template_path):
        self.templates = []
        self.template_map = {}
        
        for d in template_path:
            self.find_templates(d, [])
    
