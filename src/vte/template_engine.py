from jinja2 import *
from vte.template_rgy import TemplateRgy, TemplateInfo
from jinja2.loaders import FileSystemLoader

class TemplateEngine:

    # template: TemplateInfo
    def __init__(self, outdir, template):
        self.outdir = outdir
        self.template = template
        templLoader = FileSystemLoader();
        self.env = Environment(loader=templLoader)
       
    def generate(self):
        print "Generate"