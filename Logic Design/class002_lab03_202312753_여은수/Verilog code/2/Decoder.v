`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:59:40 04/23/2024 
// Design Name: 
// Module Name:    Decoder 
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
`include "V74x139h_b.v"

module Decoder(
    input G,
    input [2:0] a,
    output [7:0] y
);

    wire [7:0] y_internal;

    V74x139h_b T1(.G_L(~a[2]), .A(a[0]), .B(a[1]), .Y(y_internal[7:4]));
    V74x139h_b T2(.G_L(a[2]), .A(a[0]), .B(a[1]), .Y(y_internal[3:0]));

    assign y = ~y_internal;

endmodule
