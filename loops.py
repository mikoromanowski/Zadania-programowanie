
# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
result = []

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        result.append(num)

print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:", result)


'''
# 2. Write a Python program to construct the following pattern, using a nested for loop.
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*
rows = 5

for i in range(1, rows * 2):
    if i <= rows:
        print('* ' * i)
    else:
        print('* ' * (2 * rows - i))

# 3. Write a Python program that accepts a word from the user and reverses it.
word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")

print("\n")

# 4. Write a Python program to count the number of even and odd numbers in a series of numbers
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count_odd = 0
count_even = 0

for x in numbers:
    if not x % 2:  
        count_even += 1
    else:
        count_odd += 1

print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd) 

# 5. Write a Python program that prints each item and its corresponding type from the following list.
#Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in datalist:
    print("Item:", item, "| Type:", type(item))

# 6. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5
for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num, end=' ')

# 7. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
lines = []
print("Enter lines (press Enter twice to end):")
while True:
    line = input()
    if not line:
        break
    lines.append(line)

print("\nOutput:")
for line in lines:
    print(line.lower())

# 8. Write a  Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
#Sample Data : 0100,0011,1010,1001,1100,1001
#Expected Output : 1010
def binary_divisible_by_5(binary_sequence):
    numbers = binary_sequence.split(',')
    divisible_by_5 = []

    for binary_num in numbers:
        decimal_num = int(binary_num, 2)
        if decimal_num % 5 == 0:
            divisible_by_5.append(binary_num)

    return ','.join(divisible_by_5)

sample_data = "0100,0011,1010,1001,1100,1001"

print(binary_divisible_by_5(sample_data))

# 9. Write a Python program that accepts a string and calculates the number of digits and letters.
#Sample Data : Python 3.2
#Expected Output :
#Letters 6
#Digits 2
def count_letters_and_digits(inputing):
    letters = 0
    digits = 0
    for char in inputing:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits

sample_data = "Python 3.2"
letter_count, digit_count = count_letters_and_digits(sample_data)
print("Letters:", letter_count)
print("Digits:", digit_count)

# 10. Write a  Python program to check the validity of passwords input by users.
#Validation :
#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.
import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    
    return True

password = input("Enter password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")

# 11. Write a  Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
def are_all_digits_even(number):
    for digit in str(number):
        if int(digit) % 2 != 0:
            return False
    return True

even_digit_numbers = []

for num in range(100, 401):
    if are_all_digits_even(num):
        even_digit_numbers.append(str(num))

result = ', '.join(even_digit_numbers)
print(result)

# 12. Write a Python program to print the alphabet pattern 'A'.
#Expected Output:
 # ***                                                                   
 #*   *                                                                  
 #*   *                                                                  
 #*****                                                                  
 #*   *                                                                  
 #*   *                                                                  
 #*   *
result = ""
for row in range(0, 7):
  
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n"  

print(result) 

# 13. Write a  Python program to print the alphabet pattern 'D'.
#Expected Output:
 #****                                                                   
 #*   *                                                                  
 #*   *                                                                  
 #*   *                                                                  
 #*   *                                                                  
 #*   *                                                                  
 #**** 
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n"  

print(result)

# 14. Write a Python program to print the alphabet pattern 'E'.
#Expected Output:
 #*****                                                                  
 #*                                                                      
 #*                                                                      
 #****                                                                   
 #*                                                                      
 #*                                                                      
 #*****
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n"  

print(result)

# 15. Write a Python program to print the alphabet pattern 'G'.
#Expected Output:
 # ***                                                                   
 #*   *                                                                  
 #*                                                                      
 #* ***                                                                  
 #*   *                                                                  
 #*   *                                                                  
 # *** 
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n" 

print(result) 

# 16. Write a Python program to print the alphabet pattern 'L'.
#Expected Output:
 #*                                                                      
 #*                                                                      
 #*                                                                      
 #*                                                                      
 #*                                                                      
 #*                                                                      
 #*****
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or (row == 6 and column != 0 and column < 6)):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n"  
print(result)

# 17. Write a  Python program to print the alphabet pattern 'M'.
#Expected Output:
 # *       *                                                             
 # *       *                                                             
 # * *   * *                                                             
 # *   *   *                                                             
 # *       *                                                             
 # *       *                                                             
 # *       *
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
            result = result + "* "  
        else:
            result = result + "  "  

    result = result + "\n"  
print(result)

# 18. Write a Python program to print the alphabet pattern 'O'.
#Expected Output:
#  ***                                                                   
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
# *   *                                                                  
#  *** 
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n"  
print(result) 

# 19. Write a Python program to print the alphabet pattern 'P'.
#Expected Output:
# ****                                                                   
# *   *                                                                  
# *   *                                                                  
# ****                                                                   
# *                                                                      
# *                                                                      
# *  
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n"  
print(result)

# 20. Write a Python program to print the alphabet pattern 'R'.
#Expected Output:
# ****                                                                   
# *   *                                                                  
# *   *                                                                  
# ****                                                                   
# * *                                                                    
# *  *                                                                   
# *   *
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):
            result = result + "*"  
        else:
            result = result + " "  

    result = result + "\n"  
print(result) 
'''