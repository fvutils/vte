#****************************************************************************
#* vte main
#****************************************************************************

import argparse
import jinja2
import os
from . import template_rgy

def generate(args, rgy):
    print("TODO: generate_cmd")
    for t in rgy.template_map.keys():
        print("Template: " + str(t))
        env = jinja2.Environment(
            loader = rgy.template_map[t])
        
        for tmpl in env.list_templates():
            print("template: " + str(tmpl))
            template = env.get_template(tmpl)
            print("filename: " + template.module.filename)
            print("  result: " + template.render({
                "name": "foo",
                "vte_sv_header": "header"
            }))
    
def main():
    parser = argparse.ArgumentParser(prog="vte")
    subparser = parser.add_subparsers(dest="subcmd")
    generate_cmd = subparser.add_parser("generate",
        help="generate source files")
    
    generate_cmd.add_argument("template", help="ID of template")
    
    args = parser.parse_args()

    template_path = []
    template_path.append("/project/fun/vte/vte-mballance/templates")
   
    # Bring in the template path elements from 
    if os.getenv("VTE_TEMPLATE_PATH") != None:
        for elem in os.getenv("VTE_TEMPLATE_PATH").split(":"):
            template_path.append(elem)
            
    rgy = template_rgy.TemplateRgy(template_path)
    
    if args.subcmd == "generate":
        generate(args, rgy)
    

if __name__ == "__main__":
    main()

