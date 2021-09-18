
__version__ = '0.0.1'

#from vte.template_rgy import TemplateRgy, TemplateInfo
# import os
# import sys
# 
# 
# libvte_dir = os.path.dirname(os.path.realpath(__file__))
# vte_dir = os.path.dirname(libvte_dir)
# 
# print "libvte.__init__ vte_dir=", vte_dir
# 
# sys.path.insert(0, vte_dir + "/lib")


#__all__ = [
#     'TemplateRgy'
#     'TemplateInfo'
#     ]

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
      
    return str