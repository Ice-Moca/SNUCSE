`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    19:40:51 04/30/2024 
// Design Name: 
// Module Name:    Bcd_behavioral_4_30 
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
module Bcd_behavioral_4_30(
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
            1 : O = 7'b0110000;
            2 : O = 7'b1101101;
				
            3 : O = 7'b1111001;
            4 : O = 7'b0110011;
            5 : O = 7'b1011011;
				
            6 : O = 7'b1011111;
            7 : O = 7'b1111000;
            8 : O = 7'b1111111;
				
            9 : O = 7'b1111011;
            //switch off 7 segment character when the bcd digit is not a decimal number.
            default : O = 7'b0000000; 
        endcase
    end

endmodule
