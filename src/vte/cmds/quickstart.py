
import os
import sys

class CmdQuickstart(object):

    _Template = """
template:
  description: %s
  parameters: []
#   - name: param_name
#     description: param_desc
#     default: param_default
"""

    def __call__(self, args):
        if args.outdir is not None:
            outdir = args.outdir
            if not os.path.isdir(outdir):
                raise Exception("Speciifed output directory (%s) does not exist" % outdir)
        else:
            outdir = os.getcwd()

        print("Verification Template Engine Quickstart", flush=True)
        print("Template directory: %s" % outdir, flush=True)

        if os.path.isfile(os.path.join(outdir, ".vte")):
            while True:
                print("Note: pre-existing .vte file. Overwrite [yN]? ", flush=True, end="")
                line = sys.stdin.readline()
                line = line.strip()
                if line == "" or line == "n" or line == "N":
                    return # Don't overwrite
                elif line == "y" or line == "Y":
                    break
                else:
                    print("Error: expecting y|n, not %s" % line)

        print("Template Description []? ", flush=True, end="")
        line = sys.stdin.readline()
        description = line.strip()

        content = CmdQuickstart._Template % (description,)

        with open(os.path.join(outdir, ".vte"), "w") as fp:
            fp.write(content)
        
        pass