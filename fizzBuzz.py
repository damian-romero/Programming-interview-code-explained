#!/usr/bin/env python

'''
fizz buzz test with normal functions

The fizz buzz tests is aimed to check if you know how to write a function.

For a different example using lambda functions, see fizzBuzz_lambda.py
You may find useful documentation at the bottom.

© Damian Romero, 2019
Python 3.7
License: MIT license
'''

################################## Start program ##################################

# First, create a variable with input from user, aka standard input (stdin):
number = input("Tell me your integer and I\'ll fizz or buzz: ")

# Now, define the function which will evaluate the number in our variable:

def fizzbuzz(int:number): # int means the variable must be an integer

	either = 0 # this switch will help us keep track of fizz and/or buzz

	# We will use the modulo operator '%', which renders the reminder of a division.
	if ( (number%5) + (number%7) ) == 0: # if the sum of both modulos is 0:
		print("fizz-buzz")

	# If the sum is not 0, then maybe one of them is 0
	else:
		if (number%5) == 0: # check if the reminder of number /5 is 0
			print("fizz")
			either += 1 # we have found a fizz, so add +1
		if (number%7) == 0:
			print("buzz")
			either += 1 # we have found a fizz, so add +1

	# If we did not see a fizz or buzz, then tell the user:
		if not either: # 'not' will evaluate 'true' if 'either' is empty or zero:
			print("neither fizz nor buzz")


################################## Loop ##################################

# While loops keep happening as long as their condition is true:
while number.isnumeric(): # .isnumeric() is a string method to check for numbers
	# we will convert the number to an integer
	number = int(number)
	# we will pass the number to our fizzbuzz function above
	fizzbuzz(number)
	# We will ask the user for another number.
	# If the user types anything other than a number, the while loop will stop.
	number = input("\nTell me your integer and I\'ll fizz or buzz or exit with enter: ")

################################## End ##################################

'''
Documentation

To learn more about modulo and other operations, go to: https://docs.python.org/3.3/reference/expressions.html

To learn more about control flow tools such as if and while statements, go to: https://docs.python.org/3/tutorial/controlflow.html

'''