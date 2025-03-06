`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:03:13 05/14/2024 
// Design Name: 
// Module Name:    RipplecarryAdder 
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
module RipplecarryAdder(
    input c0,
    input [1:0] a,
    input [1:0] b,
    output c2,
    output [1:0] s
    );
	
	 wire c1;
	
	 fullAdder fa0(a[0],b[0],c0,s[0],c1);
	 fullAdder fa1(a[1],b[1],c1,s[1],c2);
	 
	 
endmodule
