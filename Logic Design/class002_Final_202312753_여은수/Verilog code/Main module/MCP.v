`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    22:09:01 06/16/2024 
// Design Name: 
// Module Name:    MCP 
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
module MCP(
    input [7:0] instruction,
    input clk,
    input reset,
    output reg [7:0] nextAddress,
	 output [6:0] out1,
	 output [6:0] out2,
	 output [6:0] out3,
	 output [6:0] out4
    );
	reg [7:0] register[0:3];
	reg [7:0] memory[0:31];
	reg [3:0] hd10;
	reg [3:0] hd1;
	reg [1:0] rs;
	reg [1:0] rt;
	reg [1:0] rd;
	reg signed [1:0] imm;
	wire clk1;
	FreqDivider F(.clr(reset),.clk(clk),.clkout(clk1));
	BCto7 B1(.bc(hd10),.seg(out1));
	BCto7 B2(.bc(hd1),.seg(out2));
	BCto7 B3(.bc(nextAddress[7:4]),.seg(out3));
	BCto7 B4(.bc(nextAddress[3:0]),.seg(out4));
	integer i;
	initial begin
		for(i=0;i<4;i=i+1) begin
			register[i] = 7'b0;
		end
		for(i=0;i<32;i=i+1) begin
			if(i<16) begin
				memory[i] = i;
			end
			else begin
				memory[i] = 256+16-i;
			end
		end
		hd10 = 4'b0;
		hd1 = 4'b0;
		nextAddress = 0;
	end
	always @(posedge clk1 or posedge reset) begin
		if(reset) begin
			for(i=0;i<4;i=i+1) begin
				register[i] = 8'b0;
			end
			for(i=0;i<32;i=i+1) begin
				if(i<16) begin
					memory[i] = i;
				end
				else begin
					memory[i] = 16-i;
				end
			end
			hd10 = 4'b0;
			hd1 = 4'b0;
			nextAddress = 0;
		end
		else begin
			nextAddress = nextAddress +1;
			rs = instruction[5:4];
			rt = instruction[3:2];
			imm = instruction[1:0];
			rd = instruction[1:0];
			case(instruction[7:6])
				2'b00:begin
					register[rd] = register[rs] + register[rt];
					hd10 = register[rd][7:4];
					hd1 = register[rd][3:0];
					end
				2'b01:begin
					register[rt] = memory[register[rs]+imm];
					hd10 = register[rt][7:4];
					hd1 = register[rt][3:0];
					/*
					hd10 = (register[rs]+imm)/16;
					hd1 = (register[rs]+imm)%16;
					*/
					end
				2'b10:begin
					memory[register[rs]+imm] = register[rt];
					/*
					hd10 = register[rt][7:4];
					hd1 = register[rt][3:0];
					*/
					end
				2'b11:
					nextAddress = nextAddress + imm;
			endcase
		end
	end
	

endmodule
