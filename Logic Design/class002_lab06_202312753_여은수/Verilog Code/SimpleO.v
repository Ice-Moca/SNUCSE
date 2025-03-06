`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:10:24 05/21/2024 
// Design Name: 
// Module Name:    SimpleO 
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
module SimpleO(
    input E,
    output O
    );
	 wire Eand;
	 
	 assign Eand=(E&O);
	 assign #5 O=~Eand;
	 


endmodule
