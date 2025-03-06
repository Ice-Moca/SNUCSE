`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:13:40 04/23/2024 
// Design Name: 
// Module Name:    v74x139 
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
`include "V74x139h_a.v"
`include "V74x139h_b.v"

module v74x139(
    input G1,
    input G2,
    input A1,
    input A2,
    input B1,
    input B2,
    output [3:0] Y1,
    output [3:0] Y2
    );
	
	V74x139h_a T1(.G_L(G1), .A(A1), .B(B1), .Y_L(Y1));
	V74x139h_a T2(.G_L(G2), .A(A2), .B(B2), .Y_L(Y2));

endmodule
