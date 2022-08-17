
import sys
import jinja2

class CmdPreprocess(object):

    class StringTemplateLoader(jinja2.BaseLoader):

        def __init__(self, content):
            self.content = content

        def list_templates(self):
            return ["default"]
        
        def get_source(self, environment, template):
            return self.content, "", lambda: True

    def __call__(self, args):
        if args.file == "-":
            content = sys.stdin.read()
        else:
            with open(args.file, "r") as fp:
                content = fp.read()

        loader = CmdPreprocess.StringTemplateLoader(content)
        env = jinja2.Environment(loader=loader)

        global_vars = args.parameters

        tmpl_e = env.get_template(env.list_templates()[0])

        if args.output is None or args.output == "-":
            sys.stdout.write(tmpl_e.render(global_vars))
        else:
            with open(args.output, "w") as fp:
                fp.write(tmpl_e.render(global_vars))

        pass
