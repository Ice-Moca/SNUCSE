`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:08:56 04/30/2024 
// Design Name: 
// Module Name:    KL_structural 
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
module KL_structural(
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
		
	
	wire ab,Bd,cd,BD,bcd,abcd,BcD,bCD,bcd,BCd,BCD,AD;
	and A1(ab, a,b);
	and A2(Bd,B,d);
	and A3(cd, c,d);
	and A4(BD, B, D);
	and A5(bcd, b,c,d);
	and A6(abcd, a, b,c,d );
	and A7(BcD,B,c,D);
	and A8(bCD, b, C,D);
	and A9(bcd,b,c,d)
	and A10(BCd,B,C,d)
	and A11(BCD,B,C,D)
	and A12(AD, A, D)
	
	or O1(O[0],ab);
	or O2(O[1],A,Bd,cd);
	or O3(O[2],A,BD,bcd);
	or O4(O[3],abcd,BcD,bCD);
	or O5(O[4],bcd,A,BcD,BCd);
	or O6(O[5],A,cd,BCD);
	or O7(O[6],B,C,AD);



endmodule
