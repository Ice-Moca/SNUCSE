`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    21:46:43 04/23/2024 
// Design Name: 
// Module Name:    mux_dataflow_ 
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
module mux_dataflow_(
    input [3:0] d,
    input s0,
    input s1,
    output y
    );
	
	wire [1:0] sel;
	assign sel={s1,s0};
	assign y = (sel==2'b00)?d[0]:
	(sel==2'b01)?d[1]:
	(sel==2'b10)?d[2]:
	(sel==2'b11)?d[3]:0;

endmodule
