# 1. Write a  Python script to sort (ascending and descending) a dictionary by value.
def sort_dict_ascending(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))
def sort_dict_descending(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
sorted_dict_ascending = sort_dict_ascending(sample_dict)
print("Dictionary sorted in ascending order by values:", sorted_dict_ascending)
sorted_dict_descending = sort_dict_descending(sample_dict)
print("Dictionary sorted in descending order by values:", sorted_dict_descending)
'''
# 2. Write a Python script to add a key to a dictionary.
d = {0: 10, 1: 20}
print(d)
d.update({2: 30})

print(d) 

# 3. Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

is_key_present(5)
is_key_present(9) 

# 4. Write a Python program to iterate over dictionaries using for loops.
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
print("Iterating over the dictionary:")
for key in sample_dict:
    print(key, "->", sample_dict[key])

# 5. Write a  Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200, 'c' : 400}
d2 = {'x': 300, 'y': 200, 'z' : 500}
d = d1.copy()
d.update(d2)

print(d) 

# 6. Write a Python program to iterate over dictionaries using for loops.
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

print("Iterating over the dictionary:")
for key in sample_dict:
    print(key, "->", sample_dict[key])

# 7. Write a Python program to sum all the items in a dictionary.
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

total_sum = 0

for value in sample_dict.values():
    total_sum += value

print("Total sum of items in the dictionary:", total_sum)

# 8. Write a Python program to multiply all the items in a dictionary.
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

total_product = 1

for value in sample_dict.values():
    total_product *= value

print("Total product of items in the dictionary:", total_product)

# 9. Write a  Python program to remove a key from a dictionary.
myDict = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
print(myDict)
if 'a' in myDict:
    del myDict['c']

print(myDict)

# 10. Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

color_dictionary = dict(zip(keys, values))

print(color_dictionary)

# 11. Write a Python program to sort a given dictionary by key.
color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}
for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
	
# 12. Write a Python program to get the maximum and minimum values of a dictionary.
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

max_value = max(sample_dict.values())

min_value = min(sample_dict.values())

print("Maximum value in the dictionary:", max_value)
print("Minimum value in the dictionary:", min_value)

# 13. Write a  Python program to get a dictionary from an object's fields.
class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

sample_object = Sample("John", 30)

dict_from_vars = vars(sample_object)
print("Dictionary from vars():", dict_from_vars)

# 14. Write a Python program to remove duplicates from the dictionary.
def remove_duplicates(original_dict):
    unique_dict = {}
    for key, value in original_dict.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    return unique_dict

sample_dict = {'apple': 5, 'banana': 2, 'orange': 5, 'grape': 1, 'kiwi': 5}

unique_dict = remove_duplicates(sample_dict)

print("Dictionary after removing duplicates:", unique_dict)

# 15. Write a Python program to check if a dictionary is empty or not.
def is_dict_empty(dictionary):
    if dictionary:
        return False
    else:
        return True

empty_dict = {}
non_empty_dict = {'apple': 5, 'banana': 2}

print("Is empty_dict empty?", is_dict_empty(empty_dict))
print("Is non_empty_dict empty?", is_dict_empty(non_empty_dict))

# 16. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1, 'kiwi': 10}
sorted_dict = sorted(sample_dict.items(), key=lambda x: x[1], reverse=True)
highest_three_values = sorted_dict[:3]

print("Highest three values and their corresponding keys:")
for key, value in highest_three_values:
    print(key, "->", value)

# 17. Write a  Python program to print a dictionary in table format.
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)

# 18. Write a Python program to convert a list into a nested dictionary of keys.
num_list = [1, 2, 3, 4]

new_dict = current = {}

for name in num_list:
    current[name] = {}
    
    current = current[name]

print(new_dict)

# 19. Write a Python program to sort a list alphabetically in a dictionary.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

sorted_dict = {x: sorted(y) for x, y in num.items()}

print(sorted_dict)

# 20. Write a  Python program to remove spaces from dictionary keys.
student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

print("Original dictionary: ", student_list)

student_dict = {x.translate({32: None}): y for x, y in student_list.items()}

print("New dictionary: ", student_dict) 
'''