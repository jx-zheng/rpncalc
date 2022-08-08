# RPNFunctions.py
# Written by Kevin Zheng
# September 2018
# Description: Contains the math implemntations of RPNCalculator

import math

stack = [0, 0, 0, 0]

def push(x):
    shift_up()
    stack[len(stack) - 1] = x

def pop():
    for i in range(len(stack) - 1, 0, -1):
        stack[i] = stack[i - 1]
    stack[0] = 0

def get_stack():
    return stack

def resize_stack(new_size):
    stack.clear()
    for _ in range(0, new_size):
        stack.append(0)

def swap():
    temp = stack[(len(stack)-2)]
    stack[(len(stack)-2)] = stack[(len(stack)-1)]
    stack[(len(stack)-1)] = temp

def zero_stack():
    for i in range(0, len(stack)):
        stack[i] = 0

def square():
    stack[(len(stack) - 1)] = math.pow(stack[(len(stack) - 1)], 2)

def power():
    exponent = stack[(len(stack) - 1)]
    base = stack[(len(stack) - 2)]
    pop() # Shift everything down so we can combine last two registers into one
    stack[(len(stack) - 1)] = math.pow(base, exponent)

def square_root():
    result = math.sqrt(stack[(len(stack) - 1)]) # raises ValueError
    stack[(len(stack) - 1)] = result

def nth_root():
    index = stack[(len(stack) - 1)]
    radicand = stack[(len(stack) - 2)]
    result = math.pow(radicand, (1/index)) # raises ZeroDivisionError
    pop()
    stack[(len(stack) - 1)] = result

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
