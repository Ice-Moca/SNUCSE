`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:01:21 04/30/2024 
// Design Name: 
// Module Name:    KL_behavioral 
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
module KL_behavioral(
		I,
		O
    );
     
     //Declare inputs,outputs and internal variables.
     input [3:0] I;
     output [6:0] O;
     reg [6:0] O;

//always block for converting bcd digit into 7 segment format
    always @(I)
    begin
        case (I) //case statement
            0 : O = 7'b1111110;
            1 : O = 7'b1000000;
				
            2 : O = 7'b1000001;
            3 : O = 7'b1001001;
				
            4 : O = 7'b0100011;
            5 : O = 7'b0011101;
				
            6 : O = 7'b0100101;
            7 : O = 7'b0010011;
				
            8 : O = 7'b0110110;
            9 : O = 7'b0110111;
            //switch off 7 segment character when the bcd digit is not a decimal number.
            default : O = 7'b0000000; 
        endcase
    end

endmodule
