## Assignment 1

# File Reader Program

This Python script reads a text file and prints its contents line by line.

## Features

- Extracts the file name from a given file path.
- Checks if the file exists before attempting to read it.
- Reads the file line by line and prints its contents.

## How to Use

1. Ensure the file `sample.txt` exists in the specified path (`../sample.txt`).
2. Run the script in a Python environment.
3. If the file exists, its contents will be printed line by line.
4. If the file is not found, an error message will be displayed.

## Example Output

```
sample.txt not found. Please check the file path.
```

OR

```
This is the first line.
This is the second line.
This is the third line.
```

## Code Explanation

- `os.path.basename(file_path)`: Extracts the file name from the path.
- `os.path.exists(file_path)`: Checks if the file exists.
- If the file exists, it is opened and read line by line.
- If the file does not exist, an error message is displayed.

## Assignment 2

# File Write and Append Program

This Python script writes user input to a file and then appends additional input to the same file.

## How to Use

1. Run the script in a Python environment.
2. Enter a value when prompted (this will overwrite `output.txt`).
3. Enter an additional value (this will be appended to `output.txt`).
4. The values will be stored in `../output.txt`.

## Example Output in `output.txt`

```
First input value
Additional appended value
```

## Notes

- The script overwrites `output.txt` with the first input.
- The second input is appended on a new line.
- Ensure the script has permission to write to `../output.txt`.
