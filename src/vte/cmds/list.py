
from vte.template_rgy import TemplateRgy

class CmdList(object):

    def __call__(self, args):
        rgy = TemplateRgy.inst()
        rgy.find_templates()

        template_ids = sorted(rgy.template_map.keys())

        max_len = 0
        for id in template_ids:
            if len(id) > max_len:
                max_len = len(id)

        fmt_str = "%-" + str(max_len) + "s - %s"
        for id in template_ids:
            print(fmt_str % (id, rgy.template_map[id].desc))
