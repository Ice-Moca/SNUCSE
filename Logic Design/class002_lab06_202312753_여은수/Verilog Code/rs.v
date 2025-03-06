`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:01:56 05/21/2024 
// Design Name: 
// Module Name:    rs 
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
module rs(
    input S,
    input R,
    output Q,
    output Qn
    );

wire Q_in,Qn_in;



assign Q_in=~(R|Qn);
assign Qn_in=~(S|Q);
assign Q=Q_in;
assign Qn=Qn_in;


endmodule
