`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:07:16 05/14/2024 
// Design Name: 
// Module Name:    fullAdder 
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
module fullAdder(
    input a,
    input b,
    input cin,
    output sum,
    output carry
    );//dataflow method
	
	assign sum=a^b^cin;
	assign carry=(a & b)|(b & cin)|(a & cin);

endmodule
