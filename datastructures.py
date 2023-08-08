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

first_set = {23, 42, 65, 57, 78, 83, 29}
print("First Set: " + str(first_set))
second_set = {57, 83, 29, 67, 73, 43, 48}
print("Second Set: " + str(second_set))
print("First Set after removing common elements: " + str(intersection_of_sets(first_set, second_set)))