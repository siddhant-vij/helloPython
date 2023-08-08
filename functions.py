import time
import math


# function to emulate a calculator based on two operands and one operator input using match case
def calculator(operand1, operand2, operator):
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            return operand1 / operand2
        case "//":
            return operand1 // operand2
        case "%":
            return operand1 % operand2
        case "**":
            return operand1**operand2
        case _:
            return "Invalid Operator"


# print(calculator(10, 20, "+"))
# print(calculator(10, 20, "-"))
# print(calculator(10, 20, "*"))
# print(calculator(10, 20, "/"))
# print(calculator(10, 20, "//"))
# print(calculator(10, 20, "%"))
# print(calculator(10, 2, "**"))
# print(calculator(10, 20, ":"))


# function to convert Decimal number to octal using print() output formatting
def decimal_to_octal(num):
    print("{:o}".format(num))


# decimal_to_octal(8)
# decimal_to_octal(10)


# function capable of greeting the user with Good Morning, Good Afternoon, and Good Evening based on current local time
def greeting():
    now = time.localtime()
    if now.tm_hour >= 0 and now.tm_hour < 12:
        print("Good Morning!")
    elif now.tm_hour >= 12 and now.tm_hour < 17:
        print("Good Afternoon!")
    else:
        print("Good Evening!")


# greeting()


# function to print even numbers between start and end
def print_even(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)


# print_even(1, 17)


# function to  print characterss from a string present at an even index number
def print_characters(string):
    str = ""
    for i in range(0, len(string), 2):
        str += string[i]
    return str


# print(print_characters("pynative"))


# function to remove first n characters from a string
def remove_characters(string, n):
    return string[n:]


# print(remove_characters("pynative", 4))


# function to return true/false if number is prime number or not
def is_prime(num):
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


# print(is_prime(7))
# print(is_prime(23045))
# print(is_prime(1000000007))


# function to print nth fibonacci number
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(3))
# print(fib(8))
# print(fib(13))


# function to reverse a string
def reverse(s):
    return s[::-1]


# print(reverse("Hello"))
# print(reverse("Hello World"))


# function to check palindrome number or not
def is_palindrome(num):
    return num == int(str(num)[::-1])


# print(is_palindrome(121))
# print(is_palindrome(125))


# function to count the total number of digits in a number
def count_digits(num):
    if num == 0:
        return 1
    num = abs(num)
    return math.floor(math.log10(num)) + 1


# print(count_digits(75869))
# print(count_digits(-75869))
# print(count_digits(0))
# print(count_digits(1))
# print(count_digits(-1))


# function to reverse an integer
def reverse(num):
    reversed_num = 0
    is_negative = num < 0

    if is_negative:
        num = -num

    while num > 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num = num // 10

    return -reversed_num if is_negative else reversed_num


# print(reverse(75869))
# print(reverse(-75869))
# print(reverse(0))
# print(reverse(1))
# print(reverse(-1))


# function to reverse each word of a string
def reverse_each_word(string):
    return " ".join([word[::-1] for word in string.split(" ")])


# print(reverse_each_word("Hello World"))
# print(reverse_each_word("My Name is Jessa"))


# a function with variable length of arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# a function to find the largest item from a given list
def find_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max


# x = [4, 6, 8, 24, 12, 2]
# print(find_max(x))


# a program to display all prime numbers within a range
def prime_range(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            print(i)


# print(prime_range(25, 50))


# Return the count of a given substring from a string
def count_substring(string, sub_string):
    return string.count(sub_string)


# print(count_substring("Emma is good developer. Emma is a writer", "Emma"))
# print(count_substring("Hello World", "World"))


# Check Palindrome Number
def is_palindrome(num):
    reverse = 0
    temp = num

    while temp > 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    return num == reverse


# print(is_palindrome(121))
# print(is_palindrome(125))


# Create a string made of the middle three characters
def get_middle(s):
    return s[len(s) // 2 - 1 : len(s) // 2 + 2]


# print(get_middle("JhonDipPeta"))
# print(get_middle("JaSonAy"))


# Append new string in the middle of a given string
def append_middle(s, word):
    return s[: len(s) // 2] + word + s[len(s) // 2 + 1 :]


# print(append_middle("Ault", "Kelly"))


# Arrange string characters such that lowercase letters in a string should come first & then the remaining uppercase letters
def arrange_string(s):
    lower = []
    upper = []
    for i in s:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    return "".join(lower + upper)


# print(arrange_string("EmmaIsAGoodDeveloper"))
# print(arrange_string("PyNaTive"))


# Count all letters, digits, and special symbols from a given string
def count_symbols(s):
    symbols = 0
    digits = 0
    letters = 0
    for i in s:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
        else:
            symbols += 1
    return letters, digits, symbols


# print(count_symbols("P@#yn26at^&i5ve"))


# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
def create_new_string(s1, s2):
    s3 = []
    p1 = 0
    p2 = len(s2) - 1

    while p1 < len(s1) or p2 >= 0:
        if p1 < len(s1):
            s3.append(s1[p1])
            p1 += 1
        if p2 >= 0:
            s3.append(s2[p2])
            p2 -= 1

    return "".join(s3)


# print(create_new_string("Abc", "Xyz"))
# print(create_new_string("AbcDef", "Xyz"))
# print(create_new_string("Abc", "LmnXyz"))


# To check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
def is_balanced(s1, s2):
    s2_set = set(s2)
    for i in s1:
        if i not in s2_set:
            return False
    return True


# print(is_balanced("Yn", "PYnative"))
# print(is_balanced("Ynf", "PYnative"))


# Calculate the sum and average of the digits present in a string
def sum_digits(s):
    sum = 0
    count = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
            count += 1
    return sum, sum / count


# print(sum_digits("PYnative29@#8496"))


# Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly').
# Create an inner function inside an outer function that will concatenate x and y.
# At last, an outer function will join the word 'developer' to it.
def outer(x, y, z):
    def inner():
        return x + y

    return inner() + z


# print(outer("Emma", "Kelly", "developer"))


# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_checker(str):
    idx = 0
    while idx < len(str) - 2:
        if idx == 0 and str[0:3] == "xyz":
            return True
        if idx != 0 and str[idx : idx + 3] == "xyz" and str[idx - 1] != ".":
            return True
        idx += 1
    return False


print(xyz_checker("abcxyz"))
print(xyz_checker("abc.xyz"))
print(xyz_checker("xyz.abc"))
