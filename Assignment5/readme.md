# Assignment Explanations

This document explains the logic and flow of both Python assignments: **Student Grades Lookup** and **Reverse First 5 Elements of a List**.

---

## Assignment 1: Student Grades Lookup Program

### Overview

This program allows the user to input a student's name and returns their grade if the student is present in the predefined dictionary. If the name is not found, it gracefully handles the error and notifies the user.

### Detailed Explanation

- A dictionary named `student_grades` is defined, where:

  - Keys are student names (e.g., `"Alice"`, `"Bob"`).
  - Values are their corresponding grades (e.g., `85`, `78`).

- The user is prompted to enter a name via `input()`.

- The program tries to look up the name in the dictionary:
  - If the name exists, it prints the grade.
  - If the name doesn't exist, a `KeyError` is raised, which is caught using a `try-except` block, and a friendly message is displayed.

### Key Concepts Used

- Dictionaries
- User input
- Error handling (`try-except`)
- String formatting with `f""`

---

## Assignment 2: Reverse First 5 Elements of a List

### Overview

This program extracts the first five elements from a list and reverses them using manual element swapping in a loop.

### Detailed Explanation

- A list `my_list` contains numbers from 1 to 10.
- A new list `new_list` is created by extracting the first five elements of `my_list` using a `for` loop.

- The list `new_list` is then reversed in place using a swapping technique:

  - An `index` pointer starts at the last position of the list (`len(new_list) - 1`).
  - The program iterates through the list, swapping elements from both ends towards the center.
  - The elements at positions `i` and `index` are swapped using:
    ```python
    new_list[i], new_list[index] = new_list[index], new_list[i]
    ```
  - After each swap, the `index` is decreased to move towards the center.

- After all swaps are complete, the reversed list is printed.

### Key Concepts Used

- Lists
- Indexing and appending
- Looping with `for`
- Two-pointer technique for reversal

---
