`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:41:07 05/14/2024 
// Design Name: 
// Module Name:    ALU1bit 
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
module ALU1bit(
    input Ai,
    input Bi,
    input M,
    input [1:0] S,
    output [5:0] Fi
    );
	
	 wire out_and,out_or,y,nAi,out_xor,out_xnor;
	 
	 assign out_and=Ai&Bi;
	 assign out_or=Ai|Bi;
	 assign nAi=~Ai;
	 assign out_xor =Ai^Bi;
	 assign out_xnor = ~(Ai^Bi);
	  
	  assign Fi[0]= (S==2'b00)?Ai:1'b0;
	  assign Fi[1]= (S==2'b01)?nAi:1'b0;
	  assign Fi[2]= (M==1'b0&S==2'b10)?out_xor:1'b0;
	  assign Fi[3]= (M==1'b0&S==2'b11)?out_xnor:1'b0;
	  assign Fi[4]= (M==1'b1&S==2'b10)?Ai^Bi:1'b0;
	  assign Fi[5]= (M==1'b1&S==2'b11)?nAi^Bi:1'b0;
					
endmodule
