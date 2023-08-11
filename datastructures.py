# Check if the first and last number of a list is the same
def is_same(list):
    return list[0] == list[-1]


# list1 = [1, 2, 3, 4, 5]
# print(is_same(list1))
# list2 = [1, 2, 3, 4, 5, 1]
# print(is_same(list2))


# Display numbers divisible by 5 from a list
def divisible_by_5(list):
    for i in list:
        if i % 5 == 0:
            print(i)


# print(divisible_by_5([10, 20, 33, 46, 55]))


# function to create a new list such that the it contains odd numbers from the first list & even numbers from the second list
def odd_even(l1, l2):
    l3 = [i for i in l1 if i % 2 != 0] + [i for i in l2 if i % 2 == 0]
    return l3


# list1 = [10, 20, 25, 30, 35, 40, 50, 51]
# list2 = [40, 45, 60, 75, 90, 23]
# print(odd_even(list1, list2))


# list comprehension which accepts items with a small letter "o" in the new list
originalList = ["Milo", "Oreo", "Choco", "Mango", "Sarah", "Olive"]
newList = [i for i in originalList if "o" in i]
# print(newList)


# list comprehension which accepts items with length greater than 4
origList = ["Milo", "Oreo", "Choco", "Mango", "Sarah", "Olive"]
newist = [i for i in origList if len(i) > 4]
# print(newist)


# to count occurrences of all characters within a string
def count_occurrences(string):
    return {i: string.count(i) for i in string}


# print(count_occurrences("Apple"))


# Remove empty strings from a list of strings
def remove_empty_strings(list):
    return [i for i in list if i]


# print(remove_empty_strings(["Apple", "", "Banana"]))
# print(remove_empty_strings(["Emma", "Jon", "", "Kelly", None, "Eric", ""]))



# Slice list into 3 equal chunks and reverse each chunk
def slice_list_into_3(lst):
    chunks = [lst[i : i + 3] for i in range(0, len(lst), 3)]
    reversed_chunks = [chunk[::-1] for chunk in chunks]
    return reversed_chunks

# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print(slice_list_into_3(sample_list))



# Count the occurrence of each element from a list & return a dictionary
def count_occurrences(list):
    return {i: list.count(i) for i in list}

# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# print(count_occurrences(sample_list))


# Create a Python set such that it shows the element from both lists in a pair
# create pairs with numbers and their squares, where the number is the key and the square is the value
# and nuber is present in list1 and square is present in list2
def create_pairs(list1, list2):
    return {(i, i ** 2) for i in list1 if i**2 in list2}

# first_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# second_list = [4, 9, 16, 25, 36, 49, 64, 23, 654, 100]
# print(create_pairs(first_list, second_list))




# Find the intersection (common) of two sets and remove those elements from the first set. Return the first set.
def intersection_of_sets(first_set, second_set):
    intersection = first_set.intersection(second_set)
    print("Common elements: " + str(intersection))
    for i in intersection:
        first_set.remove(i)
    return first_set

# first_set = {23, 42, 65, 57, 78, 83, 29}
# print("First Set: " + str(first_set))
# second_set = {57, 83, 29, 67, 73, 43, 48}
# print("Second Set: " + str(second_set))
# print("First Set after removing common elements: " + str(intersection_of_sets(first_set, second_set)))



# swap two sets
def swap_sets(first_set, second_set):
    first_set, second_set = second_set, first_set


# Check if one set is a subset or superset of another set. If found, delete all elements from that set
def is_subset(first_set, second_set):
    if first_set.issubset(second_set):
        print("First set is a subset of second set")
        first_set.clear()
    if first_set.issuperset(second_set):
        print("First set is a superset of second set")
        first_set.clear()
    return first_set

# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
# print(str(is_subset(first_set, second_set)))

# first_set = {34, 93, 22, 27, 43, 53, 48}
# second_set = {27, 43, 34} 
# print(str(is_subset(first_set, second_set)))



# Show a Value Error if a user enters a number outside the range of 5 to 9.
# If a user enters quit - this error should not be displayed.
def show_value_error():
    number = input("Enter a number between 5 and 9: ")
    if number == "quit":
        print("Thank you")
        return
    elif number.isdigit():
        number = int(number)
        if number < 5 or number > 9:
            raise ValueError("Please enter a valid number")
        else:
            print("Valid number")
    else:
        raise ValueError("Please enter a number")

# show_value_error()



# Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
def delete_element(lst, dct):
    return [i for i in lst if i in dct.values()]

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# print(delete_element(roll_number, sample_dict))



# Get all values from the dictionary and add them to a list but don’t add duplicates
def get_distinct_values(dct):
    return list(set(dct.values()))


# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# print(get_distinct_values(speed))



# Remove duplicates from a list and create a tuple and find the minimum and maximum number
def remove_duplicates(list):
    return tuple(set(list))

def min_max(list):
    return min(list), max(list)

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# print(min_max(remove_duplicates(sample_list)))



# Concatenate two lists index-wise. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
def concat_lists(list1, list2):
    new_list = [x + y for x, y in zip(list1, list2)]
    new_list += list1[len(list2):] + list2[len(list1):]
    return new_list

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# print(concat_lists(list1, list2))

# list1 = ["M", "na", "i", "Ke", "A", "B", "C"]
# list2 = ["y", "me", "s", "lly"]
# print(concat_lists(list1, list2))

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly", "A", "B", "C"]
# print(concat_lists(list1, list2))



# Given two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
def concat_lists(list1, list2):
    idx1 = 0
    idx2 = len(list2) - 1
    n1 = len(list1)
    n2 = len(list2)

    while idx1 < n1 and idx2 >= 0:
        print(list1[idx1], list2[idx2])
        idx1 += 1
        idx2 -= 1

    while idx1 < n1:
        print(list1[idx1], " ")
        idx1 += 1

    while idx2 >= 0:
        print(" ", list2[idx2])
        idx2 -= 1

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# concat_lists(list1, list2)

# list1 = [10, 20, 30, 40, 50, 60]
# list2 = [100, 200, 300, 400]
# concat_lists(list1, list2)

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400, 500, 600]
# concat_lists(list1, list2)



# Sort a tuple of tuples by 2nd item
def sort_tuple(tuple1):
    return tuple(sorted(list(tuple1), key=lambda x: x[1]))

# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# print(sort_tuple(tuple1))



# Convert two lists into a dictionary
def convert_list_to_dict(list1, list2):
    return dict(zip(list1, list2))

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(convert_list_to_dict(keys, values))



# Merge two Python dictionaries into one
def merge_dict(dict1, dict2):
    return {**dict1, **dict2}

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# print(merge_dict(dict1, dict2))



# Create a dictionary by extracting the keys from a given dictionary
def create_dict(dict1, keys):
    return {i: dict1[i] for i in keys}

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# keys = ["name", "salary"]
# print(create_dict(sample_dict, keys))



# Delete a list of keys from a dictionary
def delete_keys(dict1, keys):
    dict1 = {k: v for k, v in dict1.items() if k not in keys}
    return dict1

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys = ["name", "salary"]
# print(delete_keys(sample_dict, keys))



# Get the key of a minimum value from the following dictionary
def get_min_key(dict1):
    return min(dict1, key=dict1.get)

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(get_min_key(sample_dict))



# Read text file into a variable and replace all newlines with space
def read_file(file_name):
    with open(file_name, "r") as f:
        return f.read().replace("\n", " ")
    
# file_name = "textfile.txt"
# print(read_file(file_name))



# Remove items (greater than a number) from a list while iterating but without creating a different copy of a list
def remove_items(list, num):
    for element in list:
        if element > num:
            list.remove(element)
    return list

# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# num = 50
# print(number_list == remove_items(number_list, num))



# Reverse Dictionary mapping. Keys become values and vice versa
def reverse_dict(dict1):
    return {v: k for k, v in dict1.items()}

# ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# print(reverse_dict(ascii_dict))




# Display all duplicate items from a list
def display_duplicate_items(list1):
    return list({i for i in list1 if list1.count(i) > 1})

# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# print(display_duplicate_items(sample_list))



# Filter dictionary to contain keys present in the given list using filter() method
def filter_dict(dict1, keys):
    return dict(filter(lambda x: x[0] in keys, dict1.items()))


d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']
print(filter_dict(d1, l1))