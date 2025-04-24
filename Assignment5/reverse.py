my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []

# Extract the first 5 elements
for i in range(5):
    new_list.append(my_list[i])

print(f"Extracted First Five elements: {new_list}")

index = len(new_list) - 1

# Extract the last 5 elements in reverse order
for i in range(len(new_list)//2): 
    new_list[i],new_list[index] = new_list[index],new_list[i]
    index -= 1 

print(f"Extracted Reverse elements: {new_list}")
