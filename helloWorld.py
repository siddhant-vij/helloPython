# Hello World!
print("Hello World!")

# Shallow copy vs deep copy?

import copy

original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

original_list[2][0] = 5

print(original_list)   # Output: [1, 2, [5, 4]]
print(shallow_copy)    # Output: [1, 2, [5, 4]]
print(deep_copy)       # Output: [1, 2, [3, 4]]
