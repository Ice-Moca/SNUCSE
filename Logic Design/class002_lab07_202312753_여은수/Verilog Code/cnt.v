`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    16:02:21 05/28/2024 
// Design Name: 
// Module Name:    cnt 
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
module cnt(
    input clk,
    input rst,//external reset signal
    output [3:0] cnt10,
	 output [3:0] cnt1
    );
reg [3:0]count10;
reg [3:0]count1;
assign cnt10=count10;
assign cnt1=count1;

always @(posedge clk or posedge rst)begin
	if(rst)begin
		count10<=4'b0;
		count1<=4'b0;
	end
	else begin
		if(count10==4'b1001&count1==4'b1001)begin
			count10<=4'b0;
			count1<=4'b0;
		end
		else if(count1==4'b1001)begin
			count10<=count10+4'b1;
			count1<=4'b0;
		end
		else begin
			count1<=count1+4'b1;
		end
	end
end

endmodule
