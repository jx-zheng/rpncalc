# RPNFunctions.py
# Written by Kevin Zheng
# September 2018
# Description: Contains the math implemntations of RPNCalculator

import math

stack = [0, 0, 0, 0]
max_size = 4 # Default max size

def show_help():
    print("")
    print("- Functions of RPNCalculator - ".center(80, " "))
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
    stack[len(stack) - 1] = x

def pop():
    for i in range(len(stack) - 1, 0, -1):
        stack[i] = stack[i - 1]
    stack[0] = 0

def show_stack():
    print("=====")
    print(*stack, sep="\n")
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
        else:
            if max_size < 2:
                print("Invalid stack size: please enter a positive integer greater than 1.")
            else:
                accept_input = 1
                stack.clear()
                for _ in range(0, max_size):
                    stack.append(0)
                    if len(stack) == max_size:
                        print(f"Stack size successfully changed to {max_size} registers.")
                        break

def swap():
    temp = stack[(len(stack)-2)]
    stack[(len(stack)-2)] = stack[(len(stack)-1)]
    stack[(len(stack)-1)] = temp

def clear_stack():
    for i in range(0, max_size):
        stack[i] = 0

def square():
    stack[(len(stack) - 1)] = math.pow(stack[(len(stack) - 1)], 2)

def power():
    exponent = stack[(len(stack) - 1)]
    base = stack[(len(stack) - 2)]
    pop() # Shift everything down so that we can combine the last two registers into one register
    stack[(len(stack) - 1)] = math.pow(base, exponent)

def square_root():
    result = math.sqrt(stack[(len(stack) - 1)]) # throws ValueError
    stack[(len(stack) - 1)] = result

def nth_root():
    index = stack[(len(stack) - 1)]
    radicand = stack[(len(stack) - 2)]
    pop()
    stack[(len(stack) - 1)] = math.pow(radicand, (1/index))

def show_info():
    print("Want to learn to use RPN (Reverse Polish Notation) calculators?",
          "Visit https://www.lehigh.edu/~sgb2/rpnTutor.html (teaches you the HP-12C calculator).",
          "This program was written by Kevin Zheng.", sep="\n")

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
    numerator = stack[(len(stack) - 1)]
    denominator = stack[(len(stack) - 2)]
    result = numerator / denominator # raises ZeroDivisionError
    pop()
    stack[(len(stack) - 1)] = result

def reciprocal():
    result = 1 / stack[(len(stack) - 1)] # raises ZeroDivisionError
    stack[(len(stack) - 1)] = result

def shift_up():
    for i in range(len(stack) - 1):
        stack[i] = stack[i + 1]
    stack[len(stack) - 1] = 0

def peek():
    return stack[len(stack) - 1]
