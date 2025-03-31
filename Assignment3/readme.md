## Assignment 1

# Mathematical Functions Program

This Python script calculates various mathematical functions, including square, natural logarithm, factorial-based power computation, and sine using Taylor series expansion.

## Features

- Computes the square of a number.
- Computes the natural logarithm of a number using the Taylor series.
- Computes the sine of a number using the Taylor series.
- Uses recursion to compute the factorial of a power.

## How to Use

1. Run the script in a Python environment.
2. Enter a number when prompted.
3. The program will display the square, logarithm, and sine of the given number.

## Example Output

```
Enter a number: 5
Square of 5.0 is: 25.0
Natural logarithm of 5.0 is: 1.6094379124341003
Sine of 5.0 is : -0.9589242746631385
```

## Code Explanation

- `square(num)`: Computes and returns the square of `num`.
- `log(num, terms=100)`: Approximates the natural logarithm of `num` using the Taylor series.
- `factorialOfPower(power)`: Recursively computes the factorial of a given number.
- `sine(x, terms=10)`: Approximates the sine of `x` using the Taylor series.
- `calculate(num)`: Calls the above functions and prints the results.

## Error Handling

- The logarithm function raises an error if `num` is non-positive.
- The factorial function raises an error if `power` is negative.

## Assignment 2

# Factorial Calculator

This Python script calculates the factorial of a given number using recursion.

## Features

- Computes the factorial of a number.
- Uses recursion to calculate the factorial.

## How to Use

1. Run the script in a Python environment.
2. Enter a number when prompted.
3. The program will display the factorial of the given number.

## Example Output

```
Enter the number: 5
The factorial of 5 is 120
```

## Code Explanation

- `factorial(num)`: Recursively calculates the factorial of `num`.
- The function returns `1` if `num` is `0` or `1`, otherwise, it multiplies `num` by the factorial of `num - 1`.
- The user inputs a number, and the function computes and prints the factorial.

## Error Handling

- The script does not handle negative numbers; it assumes valid input.
