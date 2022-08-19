#****************************************************************************
#* template_rgy.py
#*
#* Registry of template info discovered based on a search list
#****************************************************************************
import os
import importlib
import pkgutil

from vte.template_info import TemplateInfo


class TemplateRgy:
    _inst = None

    def __init__(self):
        self.template_path = []
        self.templates = []
        self.template_map = {}
        self.plugin_path = []

        if os.getenv("VTE_TEMPLATE_PATH") != None:
            for elem in os.getenv("VTE_TEMPLATE_PATH").split(":"):
                self.template_path.append(elem)

        # Load plug-ins to allow them to extend the template path
        for finder,name,ispkg in pkgutil.iter_modules():
            if name.startswith("vte_ext_"):
                importlib.import_module(name)

    def find_templates(self):
        self.template_map.clear()
        self.templates.clear()

        for d in self.template_path:
            self._find_templates(d, [])

    def _find_templates(self, dir, template_id):
        
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
                    self._find_templates(
                        os.path.join(dir, d),
                        template_id)
                    template_id.pop()

    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = cls()
        return cls._inst
    
