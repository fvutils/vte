#!/usr/bin/python
#****************************************************************************
#* vte front-end
#****************************************************************************
import os
import sys

def vte_main(vte_dir, argv):
    import libvte
    import jinja2
    template_path = []
    
#    template_path.append(vte_dir + "/templates");
    print type(vte_dir)
    template_path.append(vte_dir + "/templates")
    print type(template_path[0])
    cmd = ""
   
    i=0
#    while (i<argv.length()):
#         print "ARGV: " + i + " " + argv[i]
#         i=i+1
   
    print "Hello from vte_main"
    for t in template_path:
        print "Template Path: " + t
        
    tmpl_rgy = libvte.TemplateRgy(template_path)

if __name__ == "__main__":
    vte_bindir = os.path.dirname(os.path.realpath(__file__))
    vte_dir = os.path.dirname(vte_bindir)
    
    # Initialize the library path
    sys.path.insert(0, vte_dir)
    sys.path.insert(0, vte_dir + "/lib")
#    sys.path.insert(0, vte_dir + "/libvte")
#    sys.path.insert(0, vte_dir + "/lib/jinja2")
   
    print "--> vte_main"
    vte_main(vte_dir, sys.argv)
    print "<-- vte_main"