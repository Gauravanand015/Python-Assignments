
def square(num):
  return num*num

#! This log function calculates the natural logarithm of a number using the Taylor series expansion.
def log(num,terms = 100):
  if num <= 0:
    raise ValueError("Logarithm is not defined for non-positive numbers.")
  
  y = (num-1)/(num+1)

  ln = 0
  for i in range(1,terms,2):
    ln += (1/i)*(y**i)

  return 2 * ln

def factorialOfPower(power):
  if power < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  if power == 0:
    return 1
  return factorialOfPower(power-1) * power

#! This function calculates the sine of a number using the Taylor series expansion.
#? The sine function is approximated using the Taylor series expansion, which is a mathematical representation of a function as an infinite sum of terms calculated from the values of its derivatives at a single point.
def sine(x, terms = 10):
  sin_approx = 0

  for i in range(terms):
    sign = (-1)**i
    power = 2 * i + 1
    sin_approx += sign * (x**(power)) / factorialOfPower(power)

  return sin_approx

num = float(input("Enter a number: "))
def calculate(num):
  # Calculate square
  square_result = square(num)
  print(f"Square of {num} is: {square_result}")

  # Calculate logarithm
  try:
    log_result = log(num)
    print(f"Natural logarithm of {num} is: {log_result}")
  except ValueError as e:
    print(e)

  # Calculate sine
  sine_result = sine(num)
  print(f"Sine of {num} is : {sine_result}")

calculate(num)