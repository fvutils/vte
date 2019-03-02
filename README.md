# vte
Verification Template Engine is a Jinja2-based template engine targeted at verification 
engineers. It is designed to make it easy for engineers to leverage a pre-built library
of templates for creating content, such as UVM elements (tests, sequences, agents, etc).
Also, for engineers to easily create libraries of templates to create custom content.

## Getting VTE
VTE is available as a source release on GitHub (https://github.com/fvutils/vte). 
- Download a release tarball
- Add the vte-<version>/bin directory to the PATH
- Start creating content!


## vte command
VTE usage is shown below:

```
usage: vte [-h] {generate,list} ...

positional arguments:
  {generate,list}
    generate       generate source files
    list           list available templates

optional arguments:
  -h, --help       show this help message and exit
```

### Environment Variables
The ``VTE_TEMPLATE_PATH`` environment variable is used to specify directories that contain 
templates. The path is colon-delimited.


### list command
The ``list`` sub-command shows the available templates, along with a brief description. 

Example:
```
% vte list
project.ivpm.googletest-hdl - IVPM project with Googletest-HDL dependence
verif.ip.googletest-hdl     - IP verification environment using Googletest-HDL
verif.uvm.test              - Creates a UVM test class

```


### generate command
The ``generate`` sub-command creates template content using the specified template ID.

```
usage: vte generate [-h] [-force] template name [KEY=VALUE [KEY=VALUE ...]]

positional arguments:
  template    ID of template
  name        Name to use in the template
  KEY=VALUE   Specify other template variables

optional arguments:
  -h, --help  show this help message and exit
  -force      force overwrite of existing files
```

Example:
```
% vte generate project.ivpm.googletest-hdl my_proj
Note: processing template etc/ivpm.info
Note: processing template etc/packages.mf
Note: processing template etc/env.sh
Note: processing template scripts/ivpm.py
Note: processing template scripts/ivpm.mk
% find -type f
./etc/ivpm.info
./etc/packages.mf
./etc/my_proj_env.sh
./scripts/ivpm.py
./scripts/ivpm.mk

```

# Template Structure

Elements on the ``VTE_TEMPLATE_PATH`` are considered to be repositories of templates. A 
template is identified based on the presence of a ``.vte`` file. All files in the directory
containing the ``.vte`` file and its subdirectories are assumed to be part of the template.

The template ID is derived from the directory structure between the template-path entry
and the directory containing the ``.vte`` directory. For example, the ``.vte`` file for 
the built-in template verif.uvm.test is located in the following directory:

```
verif
  uvm
    test
      .vte
```

## Template Descriptor File
The template descriptor file (``.vte`` file) conforms to Python config-file format. 
Sections are marked with ``[<section>]``, and values within the section are specified
using ``key=value`` format.


### Template Section
The template section specifies global information about the template. This section is optional.

#### Template Description
The ``desc`` entry in the ``template`` section specifies the text that will be displayed
when the user lists templates using the ``vte`` command. If this entry is not specified,
the description of the template will be blank.

Example:

```
[template]
desc = Creates a UVM test class

```

### Parameter Section
Templates can accept parameters beyond the built-in ``name`` parameter. A parameters must be
declared in the ``.vte`` file using a ``parameter`` section. The parameter name is 
specified as part of the ``parameter`` section. Example:

```
[parameter:base_class]
desc = Base class
default = uvm_test
```

The example above declares a parameter named ``base_class``. The UVM Test template uses 
this parameter as the name of the base class for the new UVM test. 


#### Parameter Description
A description of the parameter can be specified using a ``desc`` entry in the
parameter section. 


#### Parameter Default Value
A parameter can be given a default value using the ``default`` entry. For example, the
base_class parameter has a default of uvm_test. 

VTE will issue an error of the user does not provide a value for a parameter that does 
not have a default value.


## Template Files
Template files use Jinja2 format to refer to template parameters. This means that 
parameters are referenced using ``{{parameter}}`` format. Directives are specified
using ``{% directive %}`` format.

Here is an example of the template for creating a UVM test:

```
/****************************************************************************
 * {{name}}.svh
 * 
 ****************************************************************************/
{%set filename = "{{name}}.svh" %}
/**
 * Class: {{name}}
 * TODO: Document UVM Test {{name}}
 */
class {{name}} extends {{base_class}};
	`uvm_component_utils({{name}})
	
	function new(string name, uvm_component parent=null);
		super.new(name, parent);
	endfunction
	
endclass

```

Note how the built-in ``name`` parameter is used to form various identifiers in the file.
Note, also, how the template-specific ``base_class`` parameter is used to specify
the base class for the UVM test.

### filename directive
By default, VTE will create an output file that has the same name as the template file,
and is located at the same relative path in the output directory.

The output file namd and path can be changed using the ``filename`` directive. 
Template variables can be used in the value specified for the ``filename`` directive.

The UVM test template above specifies that the output filename will be the same as
the name of the UVM test class. 

### chmod directive
Often, project templates contain scripts that must be made executable. The ``chmod`` 
directive allows a template file to specify the permissions for the output file.
By default, files are created using the active umask.

Example:
The template for the ``status`` script, shown below, uses ``chmod`` to specify that 
the script must be executable.

```
#!/bin/sh
#****************************************************************************
#* status.sh
#****************************************************************************
{% set chmod = "+x" %}

testname=$1
seed=$2

if test ! -f simx.log; then
  echo "FAIL: $testname - no simx.log"
else
  n_passed=`grep "PASSED: $testname" simx.log | wc -l`
  n_failed=`grep "FAILED: $testname" simx.log | wc -l`

  if test $n_passed -eq 1 && test $n_failed -eq 0; then
    echo "PASSED: $testname"
  elif test $n_failed -ne 0; then
    echo "FAILED: $testname ($n_failed)"
  else
    echo "FAILED: $testname ($n_passed $n_failed)"
  fi
fi
```

