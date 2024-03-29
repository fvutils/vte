
import os
from setuptools import setup, find_namespace_packages

version="0.0.4"

if "BUILD_NUM" in os.environ.keys():
    version += "." + os.environ["BUILD_NUM"]

setup(
  name = "vte",
  version=version,
  packages=find_namespace_packages(where='src'),
  package_dir = {'' : 'src'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = "Template-driven content generation script focused on verification",
  long_description="""
  VTE is a Verification Template Engine for generating content for verification environments from template files and parameters.",
  """,
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL", "GoogleTest"],
  url = "https://github.com/mballance/vte",
  entry_points={
    'console_scripts': [
      'vte = vte.__main__:main'
    ]
  },
  setup_requires=[
    'setuptools_scm',
  ],
  install_requires=[
    'jinja2>=2.10',
    'jinja2-strcase',
    'pyyaml'
  ],
)

