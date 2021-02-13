# Conditionals

""" Comparison Operators
In Python, we can use comparison operators to compare values. When a comparison
is made, Python returns a boolean result, or simply a True or False. 

To check if two values are the same, we can use the equality operator: == 
To check if two values are not the same, we can use the not equals operator: != 
We can also check if values are greater than or lesser than each other using > 
and <. If you try to compare data types that aren’t compatible, like checking if 
a string is greater than an integer, Python will throw a TypeError. 

We can make very complex comparisons by joining statements together using logical 
operators with our comparison operators. These logical operators are and, or, and
not. When using the and operator, both sides of the statement being evaluated 
must be true for the whole statement to be true. When using the or operator,
if either side of the comparison is true, then the whole statement is true.
Lastly, the not operator simply inverts the value of the statement immediately
following it. So if a statement evaluates to True, and we put the not operato
in front of it, it would become False. """

# <, >, ==
print("cat" > "Cat")
print(1 == "1")

# and, or, != (not)

#Branching with if Statements if, elif, else
"""Conditionals Cheat Sheet

Comparison operators
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b
Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.
Branching blocks

In Python, we branch our code using if, else and elif. This is the branching syntax:

if condition1:
	if-block
elif condition2:
	elif-block
else:
	else-block

Remember: The if-block will be executed if condition1 is True. The elif-block will
 be executed if condition1 is False and condition2 is True. The else block will
  be executed when all the specified conditions are false."""

def is_positive(number):
  if number > 0:
    '''same like bool(true)'''
    return 1 
  else:
    return None

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

def is_positive(number):
  if number > 0:
    return True
  return False


def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color


def exam_grade(score):
	if score > 96:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))


def format_name(first_name, last_name):
	# code goes here
	if first_name != "" and last_name != "":
		string = "Name: " + last_name + " " + first_name
	elif first_name != "":
		string = "Name: " + first_name
	elif last_name != "":
		string = "Name: " + last_name
	else:
		string = ""
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
	# keep just the fractional part of the quotient
	if denominator != 0:
		return abs(numerator/denominator) - abs(int(numerator/denominator))
	return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

