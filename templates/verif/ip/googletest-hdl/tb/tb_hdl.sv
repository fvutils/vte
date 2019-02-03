/****************************************************************************
 * {{name}}_tb_hdl.sv
 ***************************************************************************/
{% set filename = "tb/{{name}}_tb_hdl.sv" %} 
module {{name}}_tb_hdl(input clock);

`ifdef HAVE_HDL_CLKGEN
	reg clk_r = 0;

	initial begin
		forever begin
			#10ns;
			clk_r <= ~clk_r;
		end
	end

	assign clock = clk_r;
`endif

	reg reset = 1;
	reg [7:0] reset_cnt = 0;

	always @(posedge clock) begin
		if (reset_cnt == 10) begin
			reset <= 0;
		end else begin
			reset_cnt <= reset_cnt + 1;
		end
	end

	
endmodule
