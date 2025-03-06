`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    16:48:10 05/28/2024 
// Design Name: 
// Module Name:    TDC 
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
module TDC(
    input Oclk,
    input reset,
    output [6:0] out10,
	 output [6:0] out1
    );
	 
	 wire clk1;//1HZ
	 wire [3:0] bcd10;
	 wire [3:0] bcd1;

	 FreqDiv F(.clr(reset),.clk(Oclk),.clkout(clk1));
	 cnt C(.clk(clk1),.rst(reset),.cnt10(bcd10),.cnt1(bcd1));
	 
	 BCDto7 B1(.bcd(bcd10),.seg(out10));
	 BCDto7 B2(.bcd(bcd1),.seg(out1));
	
endmodule
