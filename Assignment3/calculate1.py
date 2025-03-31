import math

num = float(input("Enter a number: "))

def calculate(num):
  print(f"Square of {num} is: {math.sqrt(num)}")
  print(f"Natural logarithm of {num} is: {math.log(num)}") 
  print(f"Sine of {num} is: {math.sin(num)}")


calculate(num)