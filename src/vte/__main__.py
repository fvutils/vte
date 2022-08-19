#****************************************************************************
#* vte main
#****************************************************************************

import argparse
import jinja2
import os
import stat
import sys
from stat import *
from . import template_rgy
from .cmds.generate import CmdGenerate
from .cmds.preprocess import CmdPreprocess
from .cmds.list import CmdList
from .cmds.quickstart import CmdQuickstart

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

def get_parser():
    parser = argparse.ArgumentParser(prog="vte")
    subparser = parser.add_subparsers(dest="subcmd")
    subparser.required = True

    generate_cmd = subparser.add_parser("generate",
        help="generate source files")
    generate_cmd.add_argument("-force", 
        action="store_true",
        help="force overwrite of existing files")    
    generate_cmd.add_argument("template", help="ID of template")
    generate_cmd.add_argument("name", help="Name to use in the template")
    # generate_cmd.add_argument("parameters", 
    #          metavar="KEY=VALUE", 
    #          nargs="*",
    #          help="Specify other template variables")
    generate_cmd.set_defaults(func=CmdGenerate())

    preprocess_cmd = subparser.add_parser("preprocess",
        help="Pre-process a file")
    preprocess_cmd.add_argument("-o", "--output", help="Specify output")
    preprocess_cmd.add_argument("file", help="Input file")
    preprocess_cmd.set_defaults(func=CmdPreprocess())

    list_cmd = subparser.add_parser("list",
        help="list available templates")
    list_cmd.set_defaults(func=CmdList())

    quickstart_cmd = subparser.add_parser("quickstart",
        help="Creates an initial .vte template-descriptor file")
    quickstart_cmd.add_argument("-o", "--outdir", 
        help="Specifies the output directory (default: cwd)")
    quickstart_cmd.set_defaults(func=CmdQuickstart())

    return parser

def main():
    parser = get_parser()

    parameters = {}

    # Filter out parameters first
    parse_args = []
    for arg in sys.argv:
        if arg.startswith("-D"):
            key_val = arg[2:]
            eq = key_val.find('=')
            if eq != -1:
                parameters[key_val[0:eq]] = key_val[eq+1:]
            else:
                parameters[key_val] = ""
        else:
            parse_args.append(arg)

    args = parser.parse_args(args=parse_args[1:])
    args.parameters = parameters
            
    # TODO: query extension points
   
    args.func(args)


if __name__ == "__main__":
    main()

