{%vte.header%}

/**
 * Class: {%name%}
 * TODO: Document UVM Test {%name%}
 */
class {%name%} extends {%super=uvm_test%};
	`uvm_component_utils({%name%})

	function new(string name, uvm_component parent=null);
		super.new(name, parent);
	endfunction
	
endclass
