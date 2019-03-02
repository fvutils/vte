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
