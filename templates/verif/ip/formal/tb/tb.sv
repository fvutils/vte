/****************************************************************************
 * {{name}}_tb.sv
 ****************************************************************************/
{% set filename = "{{name}}_tb.sv" %}

/**
 * Module: {{name}}_tb
 * 
 * TODO: Add module documentation
 */
module {{name}}_tb(input clock);

	reg[3:0]	reset_cnt = 0;
	reg 		reset = 1;
	
	always @(posedge clock) begin
		if (reset_cnt == 1) begin
			reset <= 0;
		end else begin
			reset_cnt <= reset_cnt + 1;
		end
	end

	// TODO: instance checker, test, and DUT
	
	{{name}}_test u_test(
			);

	// TODO: instance DUT
	
	{{name}}_checker u_checker(
		);
			
endmodule


