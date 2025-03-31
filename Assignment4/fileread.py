import os

file_path = "../sample.txt" 
file_name = os.path.basename(file_path) 

if os.path.exists(file_path):  
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
else:
    print(f"{file_name} not found. Please check the file path.")  
