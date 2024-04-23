
# 1. Write a  Python program to sum all the items in a list.
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

print(sum_list([1, 2, 4, 10, -8]))
'''
# 2. Write a  Python program to multiply all the items in a list.
def multiply_list_items(lst):
    result = 1
    for item in lst:
        result *= item
    return result
print(multiply_list_items([3, 5, 10, 2, 4]))

# 3. Write a Python program to get the largest number from a list.
def get_largest_number(lst):
    return max(lst)
print(get_largest_number([15, 100, 1000, -1000]))

# 4. Write a Python program to get the smallest number from a list.
def get_smallest_number(lst):
    return min(lst)
print(get_smallest_number([15, -10, -200, -1000]))

# 5. Write a  Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([13, 15, 14, 11, 11]))

# 6. Write a  Python program to check if a list is empty or not.
def is_list_empty(lst):
    if not lst:
        return True
    else:
        return False
print(is_list_empty([]))

# 7. Write a Python program to clone or copy a list.
first_list = [10, 22, 44, 23, 4]
new_list = list(first_list)
print(first_list)
print(new_list)

# 8. Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "Hello its me Mario"))

# 9. Write a Python function that takes two lists and returns True if they have at least one common member.
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(common_data([1, 2, 3, 4, 5, 6], [6, 7, 8, 9]))

# 10. Write a  Python program to print the numbers of a specified list after removing even numbers from it.
def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    for num in odd_numbers:
        print(num)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(print_odd_numbers(list))

# 11. Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# 12. Write a Python program to generate all permutations of a list in Python.
from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))
print(generate_permutations([3, 5, 6]))

# 13. Write a Python program to calculate the difference between the two lists.
list1 = [1, 3, 5, 6, 7, 8, 9]
list2 = [1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)

# 14. Write a Python program to access the index of a list.
nums = [5, 15, 35, 10, 8, 98, 145]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)

# 15. Write a Python program to convert a list of characters into a string.
s = ['b', 'a', 'l', 'l']
str1 = ''.join(s)
print(str1)

# 16. Write a Python program to find the index of an item in a specified list.
num = [10, 30, 4, -6]
print(num.index(4))

# 17. Write a Python program to flatten a shallow list.
import itertools
original_list = [[2, 4, 3], [1, 5, 6], [9, 20, 30, 31], [7, 9, 0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)

# 18. Write a Python program to append a list to the second list.
list1 = [1, 2, 3, 10]
list2 = ['Red', 'Green', 'Hello', 'Black']
final_list = list1 + list2
print(final_list)

# 19. Write a Python program to select an item randomly from a list.
import random
items_list = ['Ball', 'Umbrella', 'Scissors', 'Knife', 'Glass', 'Bottle']
print(random.choice(items_list))

# 20. Write a  Python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))) 

'''