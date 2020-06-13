# print("Hello World!")

# I did it!

# variable name rules

# bad practice:

# easrignbpi4e3u = 10

# awpetgertbqi3 = 20

# aerjgtalw43jt = easrignbpi4e3u * awpetgertbqi3

# print (aerjgtalw43jt)

# x = 2

# assignment statement -> you're saying what you'd like to be stored and how to reference it

# x = x + 2

# assignment with expression -> not limited to just numbers or strings etc.

# print (x)

# print function -> uses name we assigned to find value and display it on screen

# x = variable

# = = operator

# 2 = value

# print() = reserved word

# type matters

# We use strings when we want to store and refer to specific letters and numbers

#string = "Hello"

#number = 1

#string_number = "Hello " + 1

# tracebacks

# "Python prints a traceback when an exception is raised in your code."

# "A traceback is a report containing the function calls made in your code at a specific point. Tracebacks are known by many names, including stack trace, stack traceback, backtrace, and maybe others. In Python, the term used is traceback."

# "When your program results in an exception, Python will print the current traceback to help you know what went wrong."

# Tracebacks should be read from bottom to top not top to bottom like other programming languages (ex. JavaScript)

# programs flow from one step to the next -> as programmers, we provide the "paths" for the program to follow

# user input

#user_name = input('Who are you? ')

#print('Welcome', user_name)

# input gives you back a string even if you enter a number

# use int to convert input to number and perform a math

# print string and number

# lvtrflr app

# European hotel floor starts at 0, US starts at 1

# floor = input('European floor number? ')

# us_floor = int(floor) + 1

# print('US Floor:', us_floor)

# this is a tiny app! it takes an input, processes/performs a task on that input, and produces an output

# it's a simple app but an important idea: we pull some data in, we process and perform tasks using that data, and then we present the data to the user

# sequential steps

# num = 1

# print(num) # 1

# num = num + 1

# print (num) # 2

# conditional steps

# x = 5

# asking the computer a question -> is the value of x less than 10? if that's true, print "Smaller", if false, skip code

# if (x < 10):

# print("Smaller")

# is the value of x greater than 20? if that's true, print "Bigger", if false, skip code

# if (x > 20):

# print("Bigger")

# once both questions have been asked and answered, print end message

# print("All Done")

# ^ that is a whole program

#x = 4

# if(x > 2):

# print('Bigger')

# else:

# print('Smaller')

# elif

#game_count = input('How many games do you own? ')

#num_game = int(game_count)

# if num_game < 10:

#print('A small but mighty collection!')

# elif num_game < 30:

#print('A glorious collection!')

# else:

#print('Truly a collector!')

# lucky number guesser

#lucky_number = input('Guess my lucky number! ')

#num_lucky = int(lucky_number)

# if num_lucky > 9:

#print('Too high!')

# elif num_lucky < 8:

#print('Too low!')

# else:

#print('You found my lucky number!')

#print('Thanks for playing!')

# repeated steps

# blastoff

# entry point

# n = 5

# still asking a question, but instead of writing out each one, we're going to let the computer run until it's answered all of them in order (loop)

# while -> runs as long as a condition is true

# while n > 0:

# print(n)

# n = n - 1

# exit condition -> is n > then 0? when we get to n = 0, loop stops

# yes, yes, yes, yes, yes, no

# once all the questions are answered

# print("Blastoff!")

# output

# 5

# 4

# 3

# 2

# 1

# Blastoff

# beware of infinite loops! you don't want a program to run forever

# ex. i = 0

# while i <= 10:

# print("FOREVER")

# ^ This will print FOREVER to your screen until it crashes (or you hit cmd + C to stop!)

# fibonacci sequence generator

# for loop - slightly different from a while loop - reserved word

# while -> runs as long as a condition is true

# for loop -> applies a condition to each number in the series

# u, #v = 0, 1

# for i in range(0, 10):

# print(u)

# u, v = v, u + v

#start = 0

#new = 1

# for i in range(0, 10):

# can write this instead of writing out (1, 2, 3, etc.)

# for each number in 0 - 10, print out the value of the number then reassign the value of the number to the next number and add the two together

# ex. we enter the loop at 0

# we print the value of start (0)

# we reassign start from 0 to 1

# we reassign new from 1 to 0 + 1 (the sum of start and new)

# print(start)

#start, new = new, start + new

# we enter the loop at 1

# start is now 1

# new is now 1

# we reassign new to equal 1 + 1 = 2

# we go back to the beginning

# try/except

# like a try/catch block in javascript

#greeting = 'Hello world!'

# try:

#bad_code = int(greeting)

# except:

#print('Phew, that was a close one!')

#num = '8675309'

# try:

#good_code = int(num)

# except:

#print('This will not print!')

# print(num)

# try/except best practices -> don't include prints in try, code after the line that blows up will never run

#name = 'Kelly'

# try:

# print('Hello')

#num_name = int(name)

# print(name)

# except:

#num_name = -1

# print(num_name)

# try/except example with error handling

#user_string = input('Enter a number: ')

# try:

#to_num = int(user_string)

# except:

#to_num = -1

# if to_num >= 0:

#print('Nice work!')

# else:

#print('Try again!')

# functions

# blocks of reusable code - keeps from writing the same thing over and over

# def - define function

# def isn't running any code itself - just remembers it and names it whatever you want - declare a function

# definition of function

# def greeting():

# print('Hello')

# print('World')

# no output

# invoke the function

# greeting()

# print('My name is Kelly')

# greeting()

# two kinds of functions

# built-in -> provided as part of Python (ex. print(), int(), input(), etc.)

# Thanks, Guido!

# functions we define and use

# pro tip: don't name your variables after built-in functions

# def welcome(greeting, name):

# Returns a greeting

# Args:

# an argument of a function is a value that must be provided to obtain the function's result

# greeting (string): A word of welcome

# name (string): A person's name

# Returns:

# string: A greeting with a name

# f' is Python 3's way of formatting strings instead of % or str.format()

# f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values

# return f'{greeting} {name}'

# print(welcome("Hello", "Kelly"))

# I'm a real web dev!
