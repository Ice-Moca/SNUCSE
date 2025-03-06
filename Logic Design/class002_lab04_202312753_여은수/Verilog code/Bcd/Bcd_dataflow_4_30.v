`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:54:47 04/30/2024 
// Design Name: 
// Module Name:    Bcd_dataflow_4_30 
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
module Bcd_dataflow_4_30(
    I,
    O
    );
     //Declare inputs,outputs and internal variables.
     input [3:0] I;
     output [6:0] O;
     

//always block for converting bcd digit into 7 segment format
   
    assign O=
        
           I==4'b0000  ?  7'b1111110:
			  I==4'b0001  ?  7'b0110000:
			  I==4'b0010  ?  7'b1101101:
			  I==4'b0011  ?  7'b1111001:
			  I==4'b0100  ?  7'b0110011:
			  I==4'b0101  ?  7'b1011011:
			  I==4'b0110  ?  7'b1011111:
			  I==4'b0111  ?  7'b1111000:
			  I==4'b1000  ?  7'b1111111:
			  I==4'b1001  ?  7'b1111011:
			  7'b0000000;
			  
       


endmodule
