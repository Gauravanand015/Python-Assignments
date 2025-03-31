## Assignment 1

# Simple Calculator

This is a simple calculator program written in Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Adds two numbers
- Subtracts two numbers
- Multiplies two numbers
- Divides two numbers (with error handling for division by zero)

## How to Use

1. Run the script in a Python environment.
2. Enter the first number when prompted.
3. Enter the second number when prompted.
4. The program will display the results of the four arithmetic operations.

## Code Explanation

- The script defines four functions:
  - `add(a, b)`: Returns the sum of `a` and `b`.
  - `subtract(a, b)`: Returns the difference between `a` and `b`.
  - `multiply(a, b)`: Returns the product of `a` and `b`.
  - `divide(a, b)`: Returns the quotient of `a` and `b`, raising an error if `b` is zero.
- The `calculate(a, b)` function calls these arithmetic functions and prints the results.
- The script takes user input for two numbers and calls the `calculate(a, b)` function.

## Example Output

```
Enter first number: 10
Enter second number: 5
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

## Error Handling

- The division function includes error handling to prevent division by zero.
  ```python
  if b == 0:
      raise ValueError("Cannot divide by zero")
  ```
- If the user enters invalid input (non-numeric values), the script will throw an error.

## Assignment 2

# Name Greeting Program

This is a simple Python script that takes two names as input and prints a personalized greeting message.

## Features

- Takes two names as input from the user.
- Combines them into a full name.
- Prints a welcome message including the entered names.

## How to Use

1. Run the script in a Python environment.
2. Enter the first name when prompted.
3. Enter the second name when prompted.
4. The program will display a greeting message.

## Code Explanation

- The script takes user input for `first` and `second` names.
  ```python
  first = input("Enter the first name:")
  second = input("Enter the second name:")
  ```
- It then prints a greeting message using formatted strings:
  ```python
  print(f"Hi, {first} {second}! Welcome to the Python Programming Language")
  ```

## Example Output

```
Enter the first name: John
Enter the second name: Doe
Hi, John Doe! Welcome to the Python Programming Language
```
