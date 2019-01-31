#!/usr/bin/python
#****************************************************************************
#*
#****************************************************************************
import sys
import yaml

class VTETemplate(yaml.YAMLObject):
    yaml_tag = u'!VTETemplate'
    
    def __init__(self, name):
        self.name = name

def vte_main(vte_dir, argv):
    print "Hello from vte_main"

if __name__ == "main":
    vte_main("foo", sys.argv)