Reference
=========


Command Reference
-----------------

.. argparse::
    :ref: vte.__main__.get_parser
    :prog: vte


Specifying Template-Parameter Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Templates may declare and use any number of parameters. Parameter values 
may be specified on the command-line using `-DKEY=VALUE` format. Parameters
without a specified value expand to the empty string.

Custom Template Directives
--------------------------

Filename Directive
^^^^^^^^^^^^^^^^^^

By default, VTE generates an output file with the same name as each template
file. The `filename` directive provides a way for a template file to specify 
its output filename.

.. code::

    /****************************************************************************
     * {{name}}_agent_pkg.sv
     * 
     ****************************************************************************/
    {% set filename = "{{name}}_agent_pkg.sv" %}
    `include "uvm_macros.svh"


In the case above, we want to name the output file based on the value of 
the `name` parameter. All paths specified with `set filename` are relative
to the original output directory of the template file.

Template Marker-File Reference
------------------------------

The .vte file identifies the root of a VTE template directory hierarchy. In the
simplest case, it only specifies a description for the template. While this 
description can be empty (VTE uses the template identifier), it is highly
recommended to provide one.

.. code::

  template:
    description: Create a simple README

Parameter Declarations
^^^^^^^^^^^^^^^^^^^^^^

VTE templates that use template-specific parameters (ie beyond `name`) must 
specify those parameters in the .vte file. Each parameter is required to 
have a name. A description is highly recommended.

.. code::

  template:
    description: Create a simple README
    parameters: 
    - name: SUBJECT
      description: Specifies the subject of the readme
      default: "TODO: Change me"

The user must supply a value for any template parameter that doesn't have
a default value specified in its .vte file. 

