`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:12:36 05/21/2024 
// Design Name: 
// Module Name:    EdgedFF 
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
module EdgedFF(
    input S,
    input R,
    input CLK,
    output Q,
    output Qn
    );
	wire S2,R2;
	
	gatedrs #10 G(S,R,CLK,S2,R2);
	rs  #10 Rs(S2,R2,Q,Qn);

endmodule
