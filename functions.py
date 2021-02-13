""" We start a function definition with the def keyword, followed by
the name we want to give our function. After the name, we have 
the parameters, also called arguments, for the function enclosed
in parentheses. A function can have no parameters, or it can have
multiple parameters. Parameters allow us to call a function and
pass it data, with the data being available inside the function
as variables with the same name as the parameters. Lastly, we
put a colon at the end of the line.  After the colon, the function
body starts. It’s important to note that in Python the function 
body is delimited by indentation. This means that all code indented
to the right following a function definition is part of the function
body. The first line that’s no longer indented is the boundary of the
function body. It’s up to you how many spaces you use when indenting
-- just make sure to be consistent. So if you choose to indent with
four spaces, you need to use four spaces everywhere in your code. """

def greeting(name):
    print("Welcome " + name)

greeting("Angel")

def print_seconds(hours, minutes, seconds):
    print(str((hours*3600) + (minutes*60) + seconds) + " seconds")

print_seconds(1,2,3)


# Returning Values Using Functions
# Sometimes we don't want a function to simply run and finish. We may
# want a function to manipulate data we passed it and then return the
# result to us. This is where the concept of return values comes in 
# handy. We use the return keyword in a function, which tells the function
# to pass data back. When we call the function, we can store the returned
# value in a variable. Return values allow our functions to be more flexible
#     and powerful, so they can be reused and called multiple times.

# Functions can even return multiple values. Just don't forget to store all
# returned values in variables! You could also have a function return nothing "None", 
# in which case the function simply exits. 

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

def month_days(month, days):
    print(month + " has " + str(days) + " days.")

month_days("June", 30)
month_days("July", 31)

#  Self-documenting code, that will be easier to read & reuse.
def rectangle_area(base, height):
	rectangle_area = base*height  # the area is base*height
	print("The area is " + str(rectangle_area))

rectangle_area(5, 6)

# Practice functions quiz

'1
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result

print("The round-trip in kilometers is " + str(my_trip_km * 2 ))

'2
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

'3
def lucky_number(name):
  number = len(name) * 9
  lucky_number = "Hello " + name + ". Your lucky number is " + str(number)
  return lucky_number
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
