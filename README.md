# Simple Arithmetic Interpreter

## Group members
- 132049 Ongera Samson Mokaya
- 125506 June Ngumbau
- 131479 Laban Mahihu
- 124534 Charity Makhanu
- 135861 Nicole Akinyi
- 129067  Mitchelle Ashimosi
- 131497 Jerald Nyaga


This Python program serves as a basic interpreter capable of executing a set of instructions to perform simple arithmetic operations and control flow.

## Features

The interpreter supports the following features:

- Loading values onto the stack
- Storing and retrieving values in variables
- Arithmetic operations: addition, subtraction, multiplication, and division
- Conditional jumps based on a comparison
- Printing the result of operations

## Instructions

### Class: Interpreter

The `Interpreter` class has the following methods:

```python
def LOAD_VALUE(number):        # Load a numerical value onto the stack.
def STORE_NAME(name):          # Store the top value of the stack into a variable.
def LOAD_NAME(name):           # Load the value of a variable onto the stack.
def PRINT_ANSWER():            # Print the top value of the stack.
# Arithmetic Operations:
def ADD_TWO_VALUES():          # Add the top two values on the stack.
def SUBTRACT_TWO_VALUES():     # Subtract the top value from the second-top value on the stack.
def MULTIPLY_TWO_VALUES():     # Multiply the top two values on the stack.
def DIVIDE_TWO_VALUES():       # Divide the second-top value by the top value on the stack.
def COMPARE_GREATER():         # Compare the top two values on the stack and push the result onto the stack.
# Jump Operations:
def JUMP_IF_TRUE(target, instructions):  # Jump to the specified target in the instructions if the top value on the stack is true.
def JUMP(target, instructions):          # Unconditionally jump to the specified target in the instructions.
