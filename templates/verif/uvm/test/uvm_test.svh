/****************************************************************************
 * {{name}}.svh
 * 
 ****************************************************************************/
{%set filename = "{{name}}/tests/{{name}}.svh" %}
{%set chmod = "+x" %}
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
