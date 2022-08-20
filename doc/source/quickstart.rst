Quick Start
===========

VTE (Verification Template Engine) is a Python-based tool that simplifies
the task of template-driven content creation. In this section, we'll
go through the three fundamental steps for using VTE:

- Installing the tool
- Creating a template
- Using a template


Installing VTE
--------------

The easiest way to install VTE is from PyPi. 

.. code:: shell

    % python3 -m pip install --user vte

Test that you can run VTE by running the command (vte) and/or invoking
the module:

.. code:: shell

    % vte --help
    % python3 -m vte --help


Creating a Template
-------------------

VTE discovers templates by searching directories on the `VTE_TEMPLATE_PATH` 
environment variable. VTE uses a marker file named `.vte` to identify the
root of a template. All files and directories in and below a template 
directory are considered to be part of the template. The template identifier
is composed from the directory names between the directory listed in 
`VTE_TEMPLATE_PATH` and the directory containing the `.vte` marker file.

Let's look at an example to illustrate the rules.

.. code :: 

    templates
      uvm
        agent
          .vte
        component
          .vte
      doc
        blog_post
          .vte
        readme
          .vte

Let's assume we add the `templates` directory to `VTE_TEMPLATE_PATH`.
VTE will find four templates:

- uvm.agent
- uvm.component
- doc.blog_post
- doc.readme

All files in and below the directory containing the `.vte` marker will be
rendered when the template is used.

Creating the Template Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Let's create a very simple template structure. Create the following directory
structure:

.. code:: yaml

    templates
      doc
        readme

Change directory to `templates/doc/readme` and run the quickstart command:

.. code:: shell

    % vte quickstart
    Verification Template Engine Quickstart
    Template directory: templates/doc/readme
    Template Description []? Create a simple README 

This command will prompt for a description to use for the template. Enter 
a description and press `ENTER`. This will create the `.vte` marker file.

View the `.vte file`. You'll see that the initial version is quite simple.
For now, this is all we need.

.. code:: 

  template:
    description: Create a simple README
    parameters: []
  #   - name: param_name
  #     description: param_desc
  #     default: param_default


Creating the Template File
^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, let's create the template file that will be processed when we
render the template. Our `readme` template only has one file: README.md.

Create a file named `README.md` containing the following content in the
templates/doc/readme directory:

.. code:: markdown

    # README for {{name}}
    TODO: put in some content of interest

VTE supports defining and using multiple parameters,
but defines one built-in parameter that must be supplied for all 
templates: `name`. Our template file references `name` using 
Jinja2 syntax for variable references. 

We have now created a simple template for creating README.md files.


Rendering a Template
--------------------

In order to render templates, VTE must first be able to discover them.
Add the `templates` directory to the `VTE_TEMPLATE_PATH` environment
variable.

.. code:: 

    % export VTE_TEMPLATE_PATH=<path>/templates # Bourne shell
    % setenv VTE_TEMPLATE_PATH <path>/templates # csh/tsh


Let's test this out by running the `vte list` command:

.. code::

    % vte list
    doc.readme - Create a simple README

If you see the `doc.readme` line above, VTE has successfully discovered
the template.

Now, let's actually generate something. Let's create a new directory 
parallel to the `templates` directory in which to try this out

.. code::

    % mkdir scratch
    % cd scratch

Finally, let's run the generate command:

.. code::

    % vte generate doc.readme my_project
    Note: processing template README.md

VTE prints a line for each template file is processes. The output above confirms
that is processed the template README.md file.

Let's have a look at the result. View the README.md file in the scratch directory.

.. code::

    # README for my_project
    TODO: put in some content of interest

Node that the `{{name}}` reference was replaced by the name (my_project) that
we specified.

You have now created your first VTE template!

