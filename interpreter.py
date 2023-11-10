class Interpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.program_counter = 0

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def STORE_NAME(self, name):
        value = self.stack.pop()
        self.variables[name] = value

    def LOAD_NAME(self, name):
        value = self.variables.get(name, 0)
        self.stack.append(value)

    def PRINT_ANSWER(self):
        if self.stack:
            answer = self.stack.pop()
            print(answer)
        else:
            print("Error: Stack is empty. Cannot print answer.")


    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def SUBTRACT_TWO_VALUES(self):
        second_num = self.stack.pop()
        first_num = self.stack.pop()
        result = first_num - second_num
        self.stack.append(result)

    def MULTIPLY_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        result = first_num * second_num
        self.stack.append(result)

    def DIVIDE_TWO_VALUES(self):
        second_num = self.stack.pop()
        first_num = self.stack.pop()
        if second_num != 0:
            result = first_num / second_num
            self.stack.append(result)
        else:
            print("Error: Division by zero.")
    
    def COMPARE_GREATER(self):
        second_num = self.stack.pop()
        first_num = self.stack.pop()
        result = first_num > second_num
        self.stack.append(result)

    def JUMP_IF_TRUE(self, target, instructions):
        value = self.stack.pop()
        if value:
            if 0 <= target < len(instructions):
                self.program_counter = target
            else:
                print(f"Error: Invalid jump target {target}")
        else:
            self.program_counter += 1

    def JUMP(self, target, instructions):
        if 0 <= target < len(instructions):
            self.program_counter = target
        else:
            print(f"Error: Invalid jump target {target}")
        
    
    def run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        numbers = what_to_execute["numbers"]
        names = what_to_execute["names"]
        self.program_counter = 0

        while self.program_counter < len(instructions):
            each_step = instructions[self.program_counter]
            instruction, argument = each_step
            print(f"Step {self.program_counter + 1}: {instruction} {argument}")
            print(f"Stack: {self.stack}")

            if instruction == "LOAD_VALUE":
                number = numbers[argument]
                self.LOAD_VALUE(number)
            elif instruction == "STORE_NAME":
                name = names[argument]
                self.STORE_NAME(name)
            elif instruction == "LOAD_NAME":
                name = names[argument]
                self.LOAD_NAME(name)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "SUBTRACT_TWO_VALUES":
                self.SUBTRACT_TWO_VALUES()
            elif instruction == "MULTIPLY_TWO_VALUES":
                self.MULTIPLY_TWO_VALUES()
            elif instruction == "DIVIDE_TWO_VALUES":
                self.DIVIDE_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            elif instruction == "COMPARE_GREATER":
                self.COMPARE_GREATER()
            elif instruction == "JUMP_IF_TRUE":
                self.JUMP_IF_TRUE(argument, instructions)
            elif instruction == "JUMP":
                self.JUMP(argument, instructions)
            else:
                print(f"Unknown instruction: {instruction}")

            self.program_counter += 1

        print("Execution completed.")



what_to_execute = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("STORE_NAME", 0),  #store the value in the first variable (a)
        ("LOAD_VALUE", 1),
        ("STORE_NAME", 1),  #store the value in the second variable (b)
        ("LOAD_NAME", 0),
        ("LOAD_NAME", 1),
        ("ADD_TWO_VALUES", None),  # Add a and b
        ("PRINT_ANSWER", None),  # Print the addition result
        ("LOAD_NAME", 0),
        ("LOAD_NAME", 1),
        ("SUBTRACT_TWO_VALUES", None),  # Subtract b from a
        ("PRINT_ANSWER", None),  # Print the subtraction result
        ("LOAD_NAME", 0),
        ("LOAD_NAME", 1),
        ("MULTIPLY_TWO_VALUES", None),  # Multiply a and b
        ("PRINT_ANSWER", None),  # Print the multiplication result
        ("LOAD_NAME", 0),
        ("LOAD_NAME", 1),
        ("DIVIDE_TWO_VALUES", None),  # Divide a by b
        ("PRINT_ANSWER", None),  # Print the division result
    ],
    "numbers": [10, 2],
    "names": ["a", "b"]
}


# Create an instance of the Interpreter
interpreter = Interpreter()

# Run the provided code
interpreter.run_code(what_to_execute)
