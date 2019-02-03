/****************************************************************************
 * {{name}}_tb_hvl.sv
 ***************************************************************************/
`ifdef HAVE_UVM
	`include "uvm_macros.svh"
`endif

/**
 * Module: {{name}}_tb_hvl
 *
 * TODO: Add module documentation
 */
module {{name}}_tb_hvl;
	`ifdef HAVE_UVM
		import uvm_pkg::*;
		import googletest_uvm_pkg::*;
	`endif

	initial begin
		`ifdef HAVE_UVM
			run_test("googletest_uvm_test");
		`else
			googletest_sv_pkg::run_all_tests();
		`endif /* HAVE_UVM */
	end

endmodule
 