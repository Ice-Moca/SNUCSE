`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   01:05:45 06/17/2024
// Design Name:   MCP
// Module Name:   /csehome/parkted/microprocessor/mcptest.v
// Project Name:  microprocessor
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: MCP
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module mcptest;

	// Inputs
	reg [7:0] instruction;
	reg clk;
	reg reset;

	// Outputs
	wire [7:0] nextAddress;
	wire [6:0] out1;
	wire [6:0] out2;
	wire [6:0] out3;
	wire [6:0] out4;

	// Instantiate the Unit Under Test (UUT)
	MCP uut (
		.instruction(instruction), 
		.clk(clk), 
		.reset(reset), 
		.nextAddress(nextAddress), 
		.out1(out1), 
		.out2(out2), 
		.out3(out3), 
		.out4(out4)
	);
	/*
	initial begin
	clk=0;
	forever #10 clk=~clk;
	end
	*/
	initial begin
		// Initialize Inputs
		instruction = 0;
		clk = 0;
		reset = 0;
		#100;
		/*
		// Wait 100 ns for global reset to finish
		
		instruction = 8'b01001001;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction =  8'b11000001;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction =  8'b00011000;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction =  8'b10101001;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b01001101;
		#50;
      clk = 1;
		#50;
		clk=0;
		*/
		instruction = 8'b01000101;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b10000100;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b01011000;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00100111;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00111010;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00111010;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00101101;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction =  8'b10000101;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b01001101;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00011110;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b01000100;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00011010;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00011010;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00011010;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00011010;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b01101111;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00101101;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b01101001;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b00101101;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b11000001;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b0;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b01000101;
		#50;
		clk = 1;
		#50;
		clk=0;
		instruction = 8'b11101111;
		#50;
		clk = 1;
		#50;
		clk=0;
		#100
		reset=1;
		// Add stimulus here

	end
      
endmodule

