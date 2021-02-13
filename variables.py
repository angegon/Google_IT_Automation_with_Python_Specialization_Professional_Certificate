# Variables Use
base = 5
height = 3
area = (base * height)/2

print(area)

""" Multiline 
Comment"""

# Example of variables names declaration permitted,it must be started 
# by a letter or an underscore, and variable name can contains letters,
# numbers or underscore
i_am_a_variable = 1
i_am_a_variable2 = 2
_i_am_a_varible_ = 3
I_AM_A_VARIABLE = 4

print(i_am_a_variable, i_am_a_variable2, _i_am_a_varible_, I_AM_A_VARIABLE)

# Example of variables names declaraction prohibitted
# 1_i_am_a_variable <-- begin by number is not permitted
# i_am_a_variable_&_ <-- special Characters are not permitted
# print <-- Keywords or python function names are not permitted
# hi there <-- Spaces are not permitted

''' Show type 
of variables'''

print(type("Hola"))
print(type(2))
print(type(2.5))

"""
Implicit vs Explicit Conversion
Implicit conversion is where the interpreter helps us out and automatically
converts one data type into another, without having to explicitly tell it 
to do so.

By contrast, explicit conversion is where we manually convert from one data 
type to another by calling the relevant function for the data type we want 
to convert to.
"""

# Implicit conversion
print (1 + 7.5)

# Explicit conversion
number = 12
''' str convert to string'''
print("The number is :" + str(number))

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))


bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2 
print("Each person needs to pay: " + str(share))



word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " +word3 + " " +word4 + " " +word5 + " " +word6 + " " + word7)

print("2 + 2 = " + str(2 + 2))
