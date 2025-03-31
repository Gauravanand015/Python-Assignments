num1 = int(input("Enter a number: "))

def evenORodd(a):
  if a % 2 == 0:
    print(f"{a} is an even")
  else:
    print(f"{a} is odd")

evenORodd(num1)