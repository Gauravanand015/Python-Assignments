input1 = input("Enter the value: ")

with open("../output.txt", "w") as file:
    file.write(input1)


input2 =  input("Enter the additional value to append: ")
with open("../output.txt", "a") as file:
    file.write(f"\n{input2}")