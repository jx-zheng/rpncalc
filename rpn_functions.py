# RPNFunctions.py
# Written by Kevin Zheng
# September 2018
# Description: Contains the essential functions for RPNCalculator

import math
from os import system, name

stack = [0, 0, 0, 0]
max_size = 4 # Define the maximum size of the default stack

def show_help():
    print("")
    print("- Functions of RPNCalculator - ".center(80, " ")) # Centers the title using whitespace
    print("\n'help': Explains all functions and their associated commands",
          "'quit': Exit RPNCalculator",
          "'clear': Clear the screen",
          "'+', '-', '*', '/': Add, subtract, multiply, and divide; respectively",
          "'ss': Shows the stack at the time of the command execution",
          "'cs': Change the size of the stack. This will also clear the stack",
          "'sws': Swap the positions of the topmost 2 values in the stack",
          "'cls': Clear the stack",
          "'pop': Pop the topmost value from the stack",
          "'sq': Square the topmost value in the stack",
          "'^': Exponent operation with topmost 2 values in the stack",
          "'sqrt': Square root operation with the topmost value in the stack",
          "'nrt': nth root operation with the topmost two values in the stack",
          "'rec': Reciprocal operation with the topmost value in the stack",
          "'info': Show information about RPNCalculator", sep="\n")

def push(x):
    shift_up()
    stack[len(stack) - 1] = x # Set the last value in the stack to the new value input by the user

def pop():
    popholder = len(stack) - 1 # Temporarily hold the last value in the stack
    for popvalue in reversed(stack): # Iterate through the stack backwards
        stack[popholder] = stack[popholder - 1]
        popholder -= 1
        if popholder == 0: # This prevents trying to read the -1th index of the stack
            stack[0] = 0
            break

def show_stack():
    print("=====")
    print(*stack, sep="\n") # Prints each value of the stack on a new line
    print("=====")

def change_stack_size():
    global max_size
    accept_input = 0
    while accept_input == 0:
        max_size = input("Please enter a value for the stack size. ")
        try:
            max_size = int(max_size)
        except (TypeError, ValueError):
            print("Invalid stack size: please enter a positive integer greater than 1.")
            max_size = 4
        else: # If no exception was thrown when casting to integer, this executes
            if max_size < 2:
                print("Invalid stack size: please enter a positive integer greater than 1.")
            else:
                accept_input = 1
                stack.clear() # Reset all stack values to 0
                for _ in range(0, max_size):
                    stack.append(0) # Append new values to the list to change the size of the stack
                    if len(stack) == max_size:
                        print("Stack size successfully changed to {0} registers.".format(max_size))
                        break

def swap(): # Swap the values of the top two registers in the stack
    swapholder = stack[(len(stack)-2)]
    stack[(len(stack)-2)] = stack[(len(stack)-1)]
    stack[(len(stack)-1)] = swapholder

def clear_stack(): # Set all registers in the stack equal to zero
    for cleanup in range(0, max_size):
        stack[cleanup] = 0
    print("Stack cleared.")

def square():
    stack[(len(stack) - 1)] = math.pow(stack[(len(stack) - 1)], 2)

def power():
    exponent = stack[(len(stack) - 1)]
    base = stack[(len(stack) - 2)]
    pop() # Shift everything down so that we can combine the last two registers into one register
    stack[(len(stack) - 1)] = math.pow(base, exponent)

def square_root():
    try:
        stack[(len(stack) - 1)] = math.sqrt(stack[(len(stack) - 1)])
    except ValueError:
        print("Domain error (square root of negative number)")

def nth_root():
    index = stack[(len(stack) - 1)]
    radicand = stack[(len(stack) - 2)]
    pop()
    stack[(len(stack) - 1)] = math.pow(radicand, (1/index))

def show_info():
    print("Want to learn to use RPN (Reverse Polish Notation) calculators?",
          "Visit https://www.lehigh.edu/~sgb2/rpnTutor.html (teaches you the HP-12C calculator).",
          "This program was written by Kevin Zheng in 2018.", sep="\n")

def add():
    value1 = stack[(len(stack) - 1)]
    value2 = stack[(len(stack) - 2)]
    pop()
    stack[(len(stack) - 1)] = value1 + value2

def subtract():
    value1 = stack[(len(stack) - 1)]
    value2 = stack[(len(stack) - 2)]
    pop()
    stack[(len(stack) - 1)] = value2 - value1

def multiply():
    value1 = stack[(len(stack) - 1)]
    value2 = stack[(len(stack) - 2)]
    pop()
    stack[(len(stack) - 1)] = value1 * value2

def divide():
    try:
        value1 = stack[(len(stack) - 1)]
        value2 = stack[(len(stack) - 2)]
        pop()
        stack[(len(stack) - 1)] = value2 / value1
    except ZeroDivisionError:
        print("Error (Dividing by zero)")

def reciprocal():
    try:
        stack[(len(stack) - 1)] = 1 / stack[(len(stack) - 1)]
    except ZeroDivisionError:
        print("Error (Dividing by zero)")

def shift_up(): # Pops from the bottom of the stack
    stackcounter = 0
    for _ in stack:
        stack[stackcounter] = stack[stackcounter + 1]
        stackcounter += 1
        if stackcounter == (len(stack) - 1):
            stack[len(stack) - 1] = 0
            break

def print_top(): # Prints the top/last value in the stack
    print(stack[len(stack) - 1])

def clear(): # Clears console screen
    if name == 'nt': # Windows
        _ = system('cls')
    else: # Other operating sysems
        _ = system('clear')
