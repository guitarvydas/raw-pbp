# Example of Manual Use of PBP with Python

This example uses kernel0d.py as a microkernel to enact mevent-sending between two spreadsheet cells which depend upon one another. 

A GUI is displayed showing two input cells labelled A and B. Each GUI cell is a Part that has one input port called 'update' and one output port called 'user_changed'. The GUI Parts are called Agui and Bgui respectively.




Each cell is controlled by a PBP Part called PartA and PartB respective.

PartA and PartB each contain an unexported numeric variable. The value begins at 0. The value is displayed in each Part's corresponding GUI cell.

When the user types a number into cell A, PartA reacts by saving the number in a state variable and sending a mevent to PartB.
The mevent is sent using the zd.send ({port: "change", payload: "..."} where "..." is the string representation of the number that the user typed.

The mevent is queue
