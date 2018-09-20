# RPNFunctions.py
# Written by Jia Xi Zheng
# September 2018
# Description: Contains the essential functions for RPNCalculator, including math operations and stack operations.

import math
from os import system, name # Importing these functions from os in order to make use of screen clearing

Stack = [0, 0, 0, 0]
MaxSize = 4 # Define the maximum size of the default stack

def ShowHelp():
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
             "'info': Show information about RPNCalculator", sep = "\n")
        
def Push(x):
    ShiftUp()
    Stack[len(Stack) - 1] = x # Set the last value in the stack to the new value input by the user
    
def Pop():
    popholder = len(Stack) - 1 # Temporarily hold the last value in the stack
    for popvalue in reversed(Stack): # Iterate through the stack backwards
        Stack[popholder] = Stack[popholder - 1]
        popholder -= 1
        if popholder == 0: # This prevents trying to read the -1th index of the stack
            Stack[0] = 0
            break
        
def ShowStack():
    print("=====")
    print(*Stack, sep = "\n") # Prints each value of the stack on a new line
    print("=====")
    
def ChangeStackSize():
    global MaxSize # Allows us to change the value of MaxSize within this function
    AcceptInput = 0
    while (AcceptInput == 0):
        MaxSize = input("Please enter a value for the stack size. ")
        try:
            MaxSize = int(MaxSize)
        except:
            print("Invalid stack size: please enter a positive integer greater than 1.")
            MaxSize = 4
        else: # If no exception was thrown when casting to integer, this executes
            if MaxSize < 2:
                print("Invalid stack size: please enter a positive integer greater than 1.")
            else:
                AcceptInput = 1
                Stack.clear() # Reset all stack values to 0
                for ResizeStack in range(0, MaxSize):
                    Stack.append(0) # Append new values to the list to change the size of the stack
                    if len(Stack) == MaxSize:
                        print("Stack size successfully changed to {0} registers.".format(MaxSize))
                        break

def Swap(): # Swap the values of the top two registers in the stack
    swapholder = Stack[(len(Stack)-2)]
    Stack[(len(Stack)-2)] = Stack[(len(Stack)-1)]
    Stack[(len(Stack)-1)] = swapholder
    
def ClearStack(): # Set all registers in the stack equal to zero
    for cleanup in range(0, MaxSize):
        Stack[cleanup] = 0
    print("Stack cleared.")
    
def Square():
    Stack[(len(Stack) - 1)] = math.pow(Stack[(len(Stack) - 1)], 2)

def Power():
    exponent = Stack[(len(Stack) - 1)]
    base = Stack[(len(Stack) - 2)]
    Pop() # Shift everything down so that we can combine the last two registers into one register
    Stack[(len(Stack) - 1)] = math.pow(base, exponent)
    
def SquareRoot():
    try:
        Stack[(len(Stack) - 1)] = math.sqrt(Stack[(len(Stack) - 1)])
    except ValueError:
        print("Domain error (square root of negative number)")

def NthRoot():
    index = Stack[(len(Stack) - 1)]
    radicand = Stack[(len(Stack) - 2)]
    Pop()
    Stack[(len(Stack) - 1)] = math.pow(radicand, (1/index)) # Computes nth roots as numbers to the power of 1/n

def ShowInfo():
    print("Want to learn to use RPN (Reverse Polish Notation) calculators?",
         "Visit https://www.lehigh.edu/~sgb2/rpnTutor.html (teaches you in the context of the HP-12C calculator).",
         "This program was written by Jia Xi Zheng in 2018.", sep = "\n")
    
def Add():
    value1 = Stack[(len(Stack) - 1)]
    value2 = Stack[(len(Stack) - 2)]
    Pop()
    Stack[(len(Stack) - 1)] = value1 + value2

def Subtract():
    value1 = Stack[(len(Stack) - 1)]
    value2 = Stack[(len(Stack) - 2)]
    Pop()
    Stack[(len(Stack) - 1)] = value2 - value1

def Multiply():
    value1 = Stack[(len(Stack) - 1)]
    value2 = Stack[(len(Stack) - 2)]
    Pop()
    Stack[(len(Stack) - 1)] = value1 * value2

def Divide():
    try:
        value1 = Stack[(len(Stack) - 1)]
        value2 = Stack[(len(Stack) - 2)]
        Pop()
        Stack[(len(Stack) - 1)] = value2 / value1
    except ZeroDivisionError:
        print("Error (Dividing by zero)")

def Reciprocal():
    try:
        Stack[(len(Stack) - 1)] = 1 / Stack[(len(Stack) - 1)]
    except ZeroDivisionError:
        print("Error (Dividing by zero)")
    
def ShiftUp(): # Pops from the bottom of the stack
    stackcounter = 0
    for stackitem in Stack:
        Stack[stackcounter] = Stack[stackcounter + 1]
        stackcounter += 1
        if stackcounter == (len(Stack) - 1): # Prevent attempting to read out of stack bounds and zero the last register
            Stack[len(Stack) - 1] = 0
            break
            
def PrintTop(): # Prints the top/last value in the stack
    print(Stack[len(Stack) - 1])
    
def Clear(): # Clears console screen. This program tends to produce a large number of lines as output
    if name == 'nt': # Windows
        _ = system('cls') 
    else: # Other operating sysems
        _ = system('clear') 

