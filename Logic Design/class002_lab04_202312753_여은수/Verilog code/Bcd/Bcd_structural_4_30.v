`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    19:19:33 04/30/2024 
// Design Name: 
// Module Name:    Bcd_structural_4_30 
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
module Bcd_structural_4_30(
    input [3:0] I,
    output [6:0] O
    );
	 wire a,b, c,d, A, B,C, D;
		not T0(a,I[3]);
		not T1(b,I[2]);
		not T2(c,I[1]);
		not T3(d,I[0]);
		not T4(A,a);
		not T5(B,b);
		not T6(C,c);
		not T7(D,d);
		
	
	wire BcD, CD, bd, BCd, cd,bD,bC,Bc;
	and A1(BcD, B,c,D);
	and A2(CD,C,D);
	and A3(bd, b,d);
	and A4(BCd, B, C, d);
	and A5(cd, c,d);
	and A6(bD, b, D);
	and A7(bC,b,C);
	and A8(Bc, B, c);
	
	or O1(O[0],BcD, CD, bd, BCd, A);
	or O2(O[1],bD, cd, CD, bd);
	or O3(O[2],bD, BcD, cd, CD, BCd);
	or O4(O[3],BcD,bD,bd,BCd);
	or O5(O[4],bd, BCd);
	or O6(O[5],BcD,cd, A, BCd);
	or O7(O[6],bC, Bc, BCd, A);


endmodule
