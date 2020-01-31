/****************************************************************************
 * {{name}}_agent_pkg.sv
 * 
 ****************************************************************************/
{% set filename = "{{name}}_agent_pkg.sv" %} 
`include "uvm_macros.svh"

`define {{name}}_plist  #(parameter int T=0)
`define {{name}}_params #(T)
`define {{name}}_vif_t virtual {{name}}_bfm `{{name}}_params

/**
 * Package: {{name}}_agent_pkg
 * 
 * Provides the UVM {{name}} agent
 */
package {{name}}_agent_pkg;
	import uvm_pkg::*;

	`include "{{name}}_config.svh"
	`include "{{name}}_seq_item.svh"
	`include "{{name}}_driver.svh"
	`include "{{name}}_monitor.svh"
	`include "{{name}}_seq_base.svh"
	`include "{{name}}_agent.svh"
endpackage



