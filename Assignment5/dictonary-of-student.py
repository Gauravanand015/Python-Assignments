students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 65,
    "Eve": 88,
    "Frank": 74,
    "Grace": 90,
    "Hannah": 81,
    "Ivy": 95,
    "Jack": 69
}

student_name = input("Student Name: ")
try:
    print(f"{student_name}'s grade is {students[student_name]}")
except KeyError:
    print(f"{student_name} not found.")
