`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:04:53 05/21/2024 
// Design Name: 
// Module Name:    gatedrs 
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
module gatedrs(
    input S,
    input R,
    input E,
    output Q,
    output Qn
    );

	wire R_and,S_and,Q_H,Q_L;
	
	assign R_and=(R&E);
	assign S_and=(S&E);
	
	rs  RS(R_and,S_and,Q_H,Q_L);
	
	assign Q=Q_H;
	assign Qn=Q_L;
	
endmodule
