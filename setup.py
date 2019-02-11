
import os
from setuptools import setup

setup(
  name = "vte",
  packages=['vte'],
  package_dir = {'vte' : 'src/vte'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("VTE is a Verification Template Engine for generating content for verification environments from template files and parameters."),
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
    'jinja2>=2.10'
  ],
)

