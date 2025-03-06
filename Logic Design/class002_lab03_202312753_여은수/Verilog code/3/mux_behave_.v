`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    21:59:20 04/23/2024 
// Design Name: 
// Module Name:    mux_behave_ 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module mux_behave_(
    input [3:0] d,
    input s0,
    input s1,
    output y
    );
	 wire [1:0] sel;
	 reg out;
	 assign y = out;
	 assign sel = {s1,s0};
	 always@(*)
	 begin
	 case(sel)
		2'b00:out=d[0];
		2'b01:out=d[1];
		2'b10:out=d[2];
		2'b11:out=d[3];
	endcase
	end

endmodule
