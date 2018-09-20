# RPNCalculator.py
# Written by Jia Xi Zheng
# September 2018
# Description: This is the part of the RPN calculator that handles user input and calls functions from RPNFunctions.

import RPNFunctions # Importing RPNFunctions module to make everything work
import time # Importing time library to make the program startup a bit more interesting with sleep()

UserInput = "" # Initialize the user input string

print("Welcome to RPNCalculator.".center(80, " ")) # Centers the title with whitespace

time.sleep(1.5) # Pause for dramatic effect

print("For help, please enter 'help' at any time.".center(80, " "))
print("Default stack size is 4. To change the size of the stack, enter 'cs'.".center(80, " "))

while(UserInput.upper() != "QUIT"):
    UserInput = input() # Accept user input from the console
    if UserInput == "help":
        RPNFunctions.ShowHelp()
    elif UserInput.upper() == "QUIT": # Causes the exit message to be printed
        pass
    elif UserInput == "": # Pushing 0 to stack (blank or 0 input)
        RPNFunctions.Push(0)
    elif UserInput == "ss": # Print the value of all registers in the stack
        RPNFunctions.ShowStack()
    elif UserInput == "cs": # Change the number of usable registers in the stack
        RPNFunctions.ChangeStackSize()
    elif UserInput == "sws": # Swap the top two values in the stack
        RPNFunctions.Swap()
        RPNFunctions.PrintTop()
    elif UserInput == "cls": # Clear the stack by setting every register to 0
        RPNFunctions.ClearStack()
    elif UserInput == "pop": # Pop the last value from the top of the stack
        RPNFunctions.Pop()
        RPNFunctions.PrintTop()
    elif UserInput == "sq": # Square the last value in the stack
        RPNFunctions.Square()
        RPNFunctions.PrintTop()
    elif UserInput == "^": # Compute a power using the last two values in the stack
        RPNFunctions.Power()
        RPNFunctions.PrintTop()
    elif UserInput == "sqrt": # Square root the last value in the stack
        RPNFunctions.SquareRoot()
        RPNFunctions.PrintTop()
    elif UserInput == "nrt": # Compute the nth root using the last two values in the stack
        RPNFunctions.NthRoot()
        RPNFunctions.PrintTop()
    elif UserInput == "info": # Prints information about RPN Calculators to the console
        RPNFunctions.ShowInfo()
    elif UserInput == "+": # Sum of last two numbers in the stack
        RPNFunctions.Add()
        RPNFunctions.PrintTop()
    elif UserInput == "-": # Difference of last two numbers in the stack
        RPNFunctions.Subtract()
        RPNFunctions.PrintTop()
    elif UserInput == "*": # Product of last two numbers in the stack
        RPNFunctions.Multiply()
        RPNFunctions.PrintTop()
    elif UserInput == "/": # Divide last two numbers in the stack
        RPNFunctions.Divide()
        RPNFunctions.PrintTop()
    elif UserInput == "rec": # Compute the reciprocal of the last value in the stack
        RPNFunctions.Reciprocal()
        RPNFunctions.PrintTop()
    elif UserInput == "clear":
        RPNFunctions.Clear() # Clear the console screen
    else:
        try:
            RPNFunctions.Push(float(UserInput)) # If the user doesn't type a command, try to evaluate it as push
        except (TypeError, ValueError):
            print("Invalid command or value: enter 'help' for command help.")

print("Thank you for using RPNCalculator.")

