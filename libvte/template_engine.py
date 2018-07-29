from jinja2 import *
from template_rgy import TemplateRgy, TemplateInfo

class TemplateEngine:
    
    def __init__(self, outdir, template):
        self.outdir = outdir
        self.template = template
        self.env = Environment()
        
    def generate(self):
        print "Generate"