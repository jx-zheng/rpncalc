# RPNCalculator.py
# Written by Kevin Zheng
# September 2018
# Description: CLI driver for rpncalc

import rpn_functions

print("Welcome to RPNCalculator.".center(80, " ")) 
print("Enter 'help' to access a list of commands.\n".center(80, " "))

user_input = ""

while True:
    print("rpnc> ", end='')
    user_input = input().lower() # Accept user input from the console
    if user_input == "help":
        rpn_functions.show_help()
    elif user_input == "exit": 
        break
    elif user_input == "":
        rpn_functions.push(0)
    elif user_input == "ss": # Print the value of all registers in the stack
        rpn_functions.show_stack()
    elif user_input == "cs": # Change the number of usable registers in the stack
        rpn_functions.change_stack_size()
    elif user_input == "sws": # Swap the top two values in the stack
        rpn_functions.swap()
        rpn_functions.print_top()
    elif user_input == "cls": # Clear the stack by setting every register to 0
        rpn_functions.clear_stack()
    elif user_input == "pop": # Pop the last value from the top of the stack
        rpn_functions.pop()
        rpn_functions.print_top()
    elif user_input == "sq": # Square the last value in the stack
        rpn_functions.square()
        rpn_functions.print_top()
    elif user_input == "^": # Compute a power using the last two values in the stack
        rpn_functions.power()
        rpn_functions.print_top()
    elif user_input == "sqrt": # Square root the last value in the stack
        rpn_functions.square_root()
        rpn_functions.print_top()
    elif user_input == "nrt": # Compute the nth root using the last two values in the stack
        rpn_functions.nth_root()
        rpn_functions.print_top()
    elif user_input == "info": # Prints information about RPN Calculators to the console
        rpn_functions.show_info()
    elif user_input == "+": # Sum of last two numbers in the stack
        rpn_functions.add()
        rpn_functions.print_top()
    elif user_input == "-": # Difference of last two numbers in the stack
        rpn_functions.subtract()
        rpn_functions.print_top()
    elif user_input == "*": # Product of last two numbers in the stack
        rpn_functions.multiply()
        rpn_functions.print_top()
    elif user_input == "/": # Divide last two numbers in the stack
        rpn_functions.divide()
        rpn_functions.print_top()
    elif user_input == "rec": # Compute the reciprocal of the last value in the stack
        rpn_functions.reciprocal()
        rpn_functions.print_top()
    elif user_input == "clear":
        rpn_functions.clear() # Clear the console screen
    else:
        try:
            rpn_functions.push(float(user_input)) # Try to evaluate it as push
        except (TypeError, ValueError):
            print("Invalid command or value: enter 'help' for command help.")
