#1. Write a  Python program to handle a ZeroDivisionError exception when dividing a number by zero.
'''def divide_numbers(x, y):
    try:
        # Attempt to perform the division operation and store the result in the 'result' variable.
        result = x / y
        # Print the result of the division.
        print("Result:", result)
    except ZeroDivisionError:
        # Handle the exception if a division by zero is attempted.
        print("The division by zero operation is not allowed.")

# Usage
# Define the numerator and denominator values.
numerator = 100
denominator = 0
# Call the divide_numbers function with the provided numerator and denominator.
divide_numbers(numerator, denominator)

#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def get_integer_input(prompt):
    try:
        # Attempt to get an integer input from the user and store it in the 'value' variable.
        value = int(input(prompt))
        # Return the integer value.
        return value
    except ValueError:
        # Handle the exception if the user's input is not a valid integer.
        print("Error: Invalid input, input a valid integer.")

# Usage
# Call the get_integer_input function to get an integer input from the user with the provided prompt.
n = get_integer_input("Input an integer: ")
# Print the input value obtained from the function.
print("Input value:", n)

#3. Write a  Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.file
def open_file(filename):
    try:
        # Attempt to open the specified file in read mode ('r').
        file = open(filename, 'r')
        # Read the contents of the file and store them in the 'contents' variable.
        contents = file.read()
        # Print a message to indicate that the file contents will be displayed.
        print("File contents:")
        # Print the contents of the file.
        print(contents)
        # Close the file to release system resources.
        file.close()
    except FileNotFoundError:
        # Handle the exception if the specified file is not found.
        print("Error: File not found.")

# Usage
# Prompt the user to input a file name and store it in the 'file_name' variable.
file_name = input("Input a file name: ")
# Call the open_file function with the provided file name.
open_file(file_name) 

#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def get_numeric_input(prompt):
    # Use a while loop to repeatedly prompt the user until a valid numeric input is provided.
    while True:
        try:
            # Attempt to get a numeric input (float) from the user and store it in the 'value' variable.
            value = float(input(prompt))
            # Return the numeric value.
            return value
        except ValueError:
            # Handle the exception if the user's input is not a valid number.
            print("Error: Invalid input. Please Input a valid number.")

# Usage
# Call the get_numeric_input function to get the first numeric input from the user with the provided prompt.
n1 = get_numeric_input("Input the first number: ")
# Call the get_numeric_input function to get the second numeric input from the user with the provided prompt.
n2 = get_numeric_input("Input the second number: ")
# Calculate the product of the two input numbers.
result = n1 * n2
# Print the result, which is the product of the two numbers.
print("Product of the said two numbers:", result)

#5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
def open_file(filename):
    try:
        # Attempt to open the specified file in write mode ('w') using a 'with' statement.
        with open(filename, 'w') as file:
            # Try to read the contents of the file, but this code will not be executed because the file is opened in write mode.
            contents = file.read()
            # Print a message to indicate that the file contents will be displayed (this will not happen).
            print("File contents:")
            # Print the contents of the file (this will not happen).
            print(contents)
    except PermissionError:
        # Handle the exception if there is a permission denied error while opening the file.
        print("Error: Permission denied to open the file.")

# Usage
# Prompt the user to input a file name and store it in the 'file_name' variable.
file_name = input("Input a file name: ")
# Call the open_file function with the provided file name, attempting to open the file in write mode.
open_file(file_name)

#6. Write a  Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
# Define a function named test_index that takes 'data' and 'index' as parameters.
def test_index(data, index):
    try:
        # Try to access an element at the specified 'index' in the 'data' list and store it in the 'result' variable.
        result = data[index]
        # Perform desired operation using the result (in this case, printing it).
        print("Result:", result)
    except IndexError:
        # Handle the exception if the specified 'index' is out of range for the 'data' list.
        print("Error: Index out of range.")

# Define a list of numbers 'nums'.
nums = [1, 2, 3, 4, 5, 6, 7]
# Prompt the user to input an index and store it in the 'index' variable.
index = int(input("Input the index: "))
# Call the test_index function with the 'nums' list and the user-provided 'index'.
test_index(nums, index)

#7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
# Prompt the user to input a number and attempt to convert it to an integer, storing it in the 'n' variable.
try:
    n = int(input("Input a number: "))
    # If the user input is successfully converted to an integer, print the entered number.
    print("You entered:", n)
# Handle the KeyboardInterrupt exception, which occurs when the user cancels the input (typically by pressing Ctrl+C).
except KeyboardInterrupt:
    print("Input canceled by the user.")

#8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def division(dividend, divisor):
    try:
        # Try to perform the division operation and store the result in the 'result' variable.
        result = dividend / divisor
        # Print the result of the division.
        print("Result:", result)
    except ArithmeticError:
        # Handle the exception if an ArithmeticError occurs during the division operation.
        print("Error: Arithmetic error occurred!")

# Usage

# Prompt the user to input the dividend and store it as a floating-point number in the 'dividend' variable.
dividend = float(input("Input the dividend: "))
# Prompt the user to input the divisor and store it as a floating-point number in the 'divisor' variable.
divisor = float(input("Input the divisor: "))
# Call the 'division' function with the provided dividend and divisor.
division(dividend, divisor) 

#9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
def open_file(filename):
    # Prompt the user to input the file encoding (ASCII, UTF-16, UTF-8) and store it in the 'encoding' variable.
    encoding = input("Input the encoding (ASCII, UTF-16, UTF-8) for the file: ")
    try:
        # Attempt to open the file with the specified encoding in read mode and use the 'with' statement for automatic file closing.
        with open(filename, 'r', encoding=encoding) as file:
            # Read the contents of the file and store it in the 'contents' variable.
            contents = file.read()
            # Print the contents of the file.
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        # Handle the exception if a UnicodeDecodeError occurs during file reading due to an encoding issue.
        print("Error: Encoding issue occurred while reading the file.")

# Usage

# Prompt the user to input the file name and store it in the 'file_name' variable.
file_name = input("Input the file name: ")
# Call the 'open_file' function with the provided file name to open and read the file with the specified encoding.
open_file(file_name) 
'''
#10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
def test_list_operation(nums):
    try:
        # Attempt to access the 'length' attribute of the 'nums' list and assign it to 'r'.
        r = len(nums)  # Trying to access the length attribute
        # Print the length of the list 'nums'.
        print("Length of the list:", r)
    except AttributeError:
        # Handle the exception if an AttributeError occurs when attempting to access the 'length' attribute.
        print("Error: The list does not have a 'length' attribute.")

# Create a list 'nums' containing integer values.
nums = [1, 2, 3, 4, 5]
# Call the 'test_list_operation' function with the 'nums' list as a parameter to check for the 'length' attribute.
test_list_operation(nums)
