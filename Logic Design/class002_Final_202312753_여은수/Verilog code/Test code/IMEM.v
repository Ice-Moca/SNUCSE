`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    02:09:01 06/17/2024 
// Design Name: 
// Module Name:    IMEM 
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
module IMEM(
    output [7:0] instruction,
    input [7:0] Read_Address
    );
	wire [7:0] MemByte[31:0];
	assign MemByte[0] = 8'b01000101;
	assign MemByte[1] = 8'b10000100;
	assign MemByte[2] = 8'b01011000;
	assign MemByte[3] = 8'b00100111;
	assign MemByte[4] = 8'b00111010;
	assign MemByte[5] = 8'b00111010;
	assign MemByte[6] = 8'b00101101;
	assign MemByte[7] = 8'b10000101;
	assign MemByte[8] = 8'b01001101;
	assign MemByte[9] = 8'b00011110;
	assign MemByte[10] = 8'b01000100;
	assign MemByte[11] = 8'b00011010;
	assign MemByte[12] = 8'b00011010;
	assign MemByte[13] = 8'b00011010;
	assign MemByte[14] = 8'b00011010;
	assign MemByte[15] = 8'b01101111;
	assign MemByte[16] = 8'b00101101;
	assign MemByte[17] = 8'b01101001;
	assign MemByte[18] = 8'b00101101;
	assign MemByte[19] = 8'b11000001;
	assign MemByte[20] = 8'b0;
	assign MemByte[21] = 8'b01000101;
	assign MemByte[22] = 8'b11101111;
	assign instruction = MemByte[Read_Address];

endmodule
