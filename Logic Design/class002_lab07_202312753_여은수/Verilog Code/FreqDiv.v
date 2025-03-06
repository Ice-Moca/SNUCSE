`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    16:16:44 05/28/2024 
// Design Name: 
// Module Name:    FreqDiv 
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
module FreqDiv(
    input clr,
    input clk,
    output reg clkout
    );
	 reg[31:0] cnt;
	 always @(posedge clk) begin
		if(clr) begin
			cnt<=32'd0;
			clkout<=1'b0;
		end
		else if(cnt==32'd25000000)begin
			cnt<=32'd0;
			clkout<=~clkout;
		end
		else begin
			cnt<=cnt+1;
		end
	end
	 
endmodule
