# portfolio_project

steps 
{   number 6 summery
        implementation of graphical user interface to collect the input and export the output
}

{ number 6 
import tkinter
set up your window and title
set up size of window
set tk packages to collect input on button click
    ### like a = tk.entry
then button that calls back a fuction that sets
    a = tk.entry  to  b = tk. entry to collect the second input
    and changes button function (with .config) to call back the echidean fuction
then change the label with label.config(text= f"the answer is {output}")
}

first take the input "a" and "b"
assign the input "a" to variable A 
assign the input "b" to variable B 

if A is greater than B then
    ### A = B( number of B in A (X) ) + remainder(C) ###
    if remainder equal(=) zero then 
        print B 
    else loop though 
        ### X = Y( no. of y in x) + remainder(Z) ###
    until  remainder equal(=) 0 then
        print C
else
    swap the roles

code snippet corner
    how to get remainder(C)
    C = A % B
    how to get the no. of B in A(X) / Quointent
    X = A//b