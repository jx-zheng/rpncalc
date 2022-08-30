# RPNCalculator.py
# Written by Kevin Zheng
# September 2018
# Description: CLI driver for rpncalc

import rpn_functions
from os import system, name

def print_top():
    print(rpn_functions.peek())

def show_help():
    print("\n- Functions of RPNCalculator - ".center(80, " "))
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

def show_info():
    print("Want to learn to use RPN (Reverse Polish Notation) calculators?",
          "Visit https://www.lehigh.edu/~sgb2/rpnTutor.html (teaches you the HP-12C).",
          "This program was written by Kevin Zheng.", sep="\n")

def show_stack():
    print("=====")
    print(*rpn_functions.get_stack(), sep="\n")
    print("=====")

def change_stack_size():
    while True:
        size = input("Enter a value for the stack size. ")
        try:
            size = int(size)
        except (TypeError, ValueError):
            print("Invalid stack size: enter a positive integer greater than 1.")
        else:
            if size < 2:
                print("Invalid stack size: enter a positive integer greater than 1.")
            else:
                rpn_functions.resize_stack(size)
                print(f"Stack size successfully changed to {size} registers.")
                break

print("Welcome to RPNCalculator.".center(80, " ")) 
print("Enter 'help' to access a list of commands.\n".center(80, " "))

user_input = ""

while True:
    print("rpnc> ", end='')
    user_input = input().lower()

    if user_input == "help":
        show_help()

    elif user_input == "exit":
        break

    elif user_input == "":
        rpn_functions.push(0.0)

    elif user_input == "ss": # Print value of all registers in stack
        show_stack()

    elif user_input == "cs": # Change number of usable registers in stack
        change_stack_size()

    elif user_input == "sws": # Swap top two values in stack
        rpn_functions.swap()
        print_top()

    elif user_input == "cls": # Clear stack by setting every register to 0
        rpn_functions.zero_stack()
        print("Stack zeroed")

    elif user_input == "pop": # Pop last value from top of stack
        rpn_functions.pop()
        print_top()

    elif user_input == "sq": # Square last value in stack
        rpn_functions.square()
        print_top()

    elif user_input == "^": # Compute a power using last two values in stack
        rpn_functions.power()
        print_top()

    elif user_input == "sqrt": # Square root last value in stack
        try:
            rpn_functions.square_root()
        except ValueError:
            print("Error: Square root domain error")
            continue
        print_top()

    elif user_input == "nrt": # Compute nth root using last two values in stack
        try:
            rpn_functions.nth_root()
        except ZeroDivisionError:
            print("Error: Attempt to divide by zero")
            continue
        print_top()

    elif user_input == "info":
        show_info()

    elif user_input == "+": # Sum of last two numbers in stack
        rpn_functions.add()
        print_top()

    elif user_input == "-": # Difference of last two numbers in stack
        rpn_functions.subtract()
        print_top()

    elif user_input == "*": # Product of last two numbers in stack
        rpn_functions.multiply()
        print_top()

    elif user_input == "/": # Divide last two numbers in stack
        try:
            rpn_functions.divide()
        except ZeroDivisionError:
            print("Error: Attempt to divide by zero")
            continue
        print_top()

    elif user_input == "rec": # Compute reciprocal of last value in stack
        try: 
            rpn_functions.reciprocal()
        except ZeroDivisionError:
            print("Error: Attempt to divide by zero")
            continue
        print_top()

    elif user_input == "clear":
        if name == 'nt': # Windows
            system('cls')
        else:
            system('clear')

    else:
        try:
            rpn_functions.push(float(user_input))
        except (TypeError, ValueError):
            print("Invalid command or value: enter 'help' for commands.")
