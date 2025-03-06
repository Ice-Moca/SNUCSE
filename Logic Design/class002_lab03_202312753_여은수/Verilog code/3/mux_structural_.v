`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    21:46:02 04/23/2024 
// Design Name: 
// Module Name:    mux_structural_ 
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
module mux_structural_(
    input [3:0] d,
    input s0,
    input s1,
    output y
    );
	wire a,b,c,D,e,f;
	wire ns0,ns1;
	not T6(ns0,s0);
	not T7(ns1,s1);
	and T1(a,ns0,d[0],ns1);
	and T2(b,s0,d[1],ns1);
	and T3(c,ns0,d[2],s1);
	and T4(D,s0,d[3],s1);
	or T5(y,a,b,c,D);
endmodule
