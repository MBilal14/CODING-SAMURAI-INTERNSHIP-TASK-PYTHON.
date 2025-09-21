# 🧮 Project 1: Simple Calculator
# 📘 Description:
# A command-line calculator that performs basic operations:
# addition, subtraction, multiplication, and division.
# 🛠 Skills: Functions, user input, basic syntax, operators


# Function for addition
def addition(num1: int, num2: int) -> int:
    return num1 + num2


# Function for subtraction
def subtraction(num1: int, num2: int) -> int:
    return num1 - num2


# Function for multiplication
def multiplication(num1: int, num2: int) -> int:
    return num1 * num2


# Function for division (integer division)
def division(num1: int, num2: int) -> int:
    return num1 // num2  # Use // for integer result


# --- Main Program Execution ---
# Ask the user for two numbers
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

# Perform operations
add = addition(number1, number2)
sub = subtraction(number1, number2)
mul = multiplication(number1, number2)
div = division(number1, number2)

# Display results
print(f"Addition of two numbers = {add}")
print(f"Subtraction of two numbers = {sub}")
print(f"Multiplication of two numbers = {mul}")
print(f"Division of two numbers = {div}")
