#****************************************************************************
#* template_rgy.py
#*
#* Registry of template info discovered based on a search list
#****************************************************************************
import os
import yaml

class TemplateInfo:
    def __init__(self, name, tmpl_id, tmpl_dir):
        print "template_info::init"
        self.name = name
        self.tmpl_id = tmpl_id
        self.tmpl_dir = tmpl_dir

class TemplateRgy:
    def find_templates(self, path):
        print "find_templates ", path
        print type(path)
        if os.path.isfile(os.path.join(path, ".vte")):
            # Found a template
            self.process_template(path)
        elif os.path.isdir(path):
            # Process subdirectories
            print "os.walk"
            for root, dirs, d in os.walk(path, followlinks=True):
                self.find_templates(d)
                
        else:
            print "Error: neither template dir nor directory"
            

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
        
        tmpl = TemplateInfo(name, dflt_template_id, path)
       
        print "Type ", type(dot_vte)
        
        for key in dot_vte.keys():
            print "key: ", key
             
        print "Process template ", root_path, " ", path, " ", dflt_template_id
        
    def __init__(self, template_path):
        print "template_rgy::init ", len(template_path)
        for d in template_path:
            for target_dir, subdirs, files in os.walk(d, followlinks=True):
                print "Target dir: ", target_dir
                if (os.path.isfile(os.path.join(target_dir, ".vte"))):
                    self.process_template(d, target_dir)
                
                
            print "find_template: " + d
            print type(d)
#            self.find_templates(d)
    
