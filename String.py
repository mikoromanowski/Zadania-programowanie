#1. Write a  Python program to calculate the length of a string.
def string_length(string):
    length = 0
    for char in string:
        length += 1
    return length
print(string_length('Jamaica'))
'''
#2. Write a Python program to count the number of characters (character frequency) in a string.
def count_characters(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency
print(count_characters('google.com'))

#3. Write a Python program to remove the nth index character from a nonempty string.
def remove_character(string, n):
    if n < 0 or n >= len(string):
        return "Invalid index"
    else:
        return string[:n] + string[n+1:]
print(remove_character('Python', 3)) 

#4. Write a  Python program to change a given string to a newly string where the first and last chars have been exchanged.
def exchange_first_and_last(string):
    if len(string) < 2:
        return string  # If the string has less than 2 characters, no change is made
    else:
        return string[-1] + string[1:-1] + string[0]
print(exchange_first_and_last('bones'))

#5. Write a Python program to remove characters that have odd index values in a given string.
def remove_odd_index_characters(string):
    return ''.join([char for index, char in enumerate(string) if index % 2 == 0])
print(remove_odd_index_characters('Jamaica'))

#6. Write a Python program to count the occurrences of each word in a given sentence.
def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
print(count_word_occurrences('Who let the dogs out ? Who ? Who ? Who ?'))

#7. Write a  Python function to reverse a string if its length is a multiple of 4.
def reverse_string_if_multiple_of_four(string):
    if len(string) % 4 == 0:
        return string[::-1]  # Reverses the string
    else:
        return string
print(reverse_string_if_multiple_of_four('charisma'))

#8. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def convert_to_uppercase(string):
    if sum(1 for char in string[:4] if char.isupper()) >= 2:
        return string.upper()
    else:
        return string
print(convert_to_uppercase('BaSketball'))

#9. Write a  Python program to sort a string lexicographically.
def lexicographic_sort(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string
print(lexicographic_sort('Basketball'))

#10. Write a Python program to remove a newline in Python.
def remove_newline(string):
    return string.rstrip('\n')
print(remove_newline('Scotland forever\n'))

#11. Write a Python program to check whether a string starts with specified characters.
string = "Basketball"
print(string.startswith("Bas"))

#12. Write a Python program to print the following numbers up to 2 decimal places.
def print_numbers(numbers):
    for number in numbers:
        print("{:.2f}".format(number))
numbers = [3.56789, 12.34567, 5.643]
print_numbers(numbers)

#13. Write a Python program to print the following numbers up to 2 decimal places with a sign.
def print_numbers_with_sign(numbers):
    for number in numbers:
        if number >= 0:
            print("+{:.2f}".format(number))
        else:
            print("{:.2f}".format(number))
numbers = [3.1456, -2.2313, 9.3456, -1.2341]
print_numbers_with_sign(numbers)

#14. Write a Python program to print the following positive and negative numbers with no decimal places.
def print_whole_numbers(numbers):
    for number in numbers:
        if number >= 0:
            print("{:+.0f}".format(number))
        else:
            print("{:.0f}".format(number))
numbers = [3.1456, -2.2313, 9.3456, -1.2341, 4.324234]
print(print_whole_numbers(numbers))

#15. Write a Python program to find the first repeated character in a given string.
def first_repeated_char(str1):
    for index, c in enumerate(str1):
        if str1[:index + 1].count(c) > 1:
            return c  
    return "None"  
print(first_repeated_char("Basketball"))
print(first_repeated_char("Poker")) 

#16. Write a Python program to find the first repeated word in a given string.
def first_repeated_word(str1):
    temp = set()
    for word in str1.split():
        if word in temp:
            return word  
        else:
            temp.add(word)  
    return 'None'  
print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc")) 

#17. Write a Python program to find the second most repeated word in a given string.
def word_count(str):
    counts = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1  
        else:
            counts[word] = 1  
    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    return counts_x[-2]
print(word_count('I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.'))

#18. Write a  Python program to remove spaces from a given string.
def remove_spaces(string):
    return ''.join(string.split())
print(remove_spaces('Basket ball'))

#19. Write a Python program to move spaces to the front of a given string.
def move_Spaces_front(str1):
    noSpaces_char = [ch for ch in str1 if ch != ' ']
    spaces_char = len(str1) - len(noSpaces_char)
    result = ' ' * spaces_char
    result = '"' + result + ''.join(noSpaces_char) + '"'

    return result  
print(move_Spaces_front('google . com'))

#20. Write a Python program to find the maximum number of characters in a given string.
def max_character_count(string):
    max_count = 0
    for char in string:
        max_count = max(max_count, string.count(char))
    return max_count

input_string = "Patton"
result = max_character_count(input_string)
print("Maximum number of characters:", result)
'''