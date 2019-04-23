
{%set filename = "tb/env/{{name}}_env_pkg.sv" %}
`include "uvm_macros.svh"

package {{name}}_env_pkg;
	import uvm_pkg::*;

	`include "{{name}}_env.svh"
	
endpackage
