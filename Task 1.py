"""
==========================================
Aenexz Tech
Data Analysis Internship

Python Assignment Solutions

Submitted by: Narbavee
Date: 19/07/2026
==========================================
"""

# 1. Find the largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# 2. Check whether a given year is a leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# 3. Check if a character is a vowel or consonant

char = input("Enter a single letter: ")

vowels = "aeiouAEIOU"

if len(char) == 1 and char.isalpha():
  
    if char in vowels:
        print(f"'{char}' is a Vowel")
    else:
        print(f"'{char}' is a Consonant")
else:
    print("Invalid input, please enter exactly one letter")


# 4. Check whether a number is divisible by both 5 and 11

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# 5. Calculate the sum of first N natural numbers using a while loop

n = int(input("Enter N: "))

total_sum = 0
i = 1

while i <= n:
    total_sum += i
    i += 1

print(f"The sum of the first {n} natural numbers is : {total_sum}")

# 6. Print the multiplication table of a given number using a while loop

num = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# 7. Print a pyramid pattern

rows = 4

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Output:

#    *
#   ***
#  *****
# *******

# 8. Print the pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Output:

# 1
# 12
# 123
# 1234
# 12345

# 1. Function to find the area of a circle

def area(radius):
    return 3.14 * radius * radius

r = float(input("Enter the radius: "))
result = area(r)
print("Area of the circle is:", result)

# 2. Function to find the largest of three numbers

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number is:", largest(a, b, c))


# 3. Function to find the length of a string without using len()

def string_length(text):
    count = 0
    for i in text:
        count = count + 1
    return count

text = input("Enter a string: ")
print("Length of the string is:", string_length(text))

# 4. Function to check whether a number is prime

def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

# 5. Recursive function to find the nth Fibonacci number

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the value of n: "))
print("Fibonacci number is:", fibonacci(n))

# 6. Recursive function to reverse a string

def reverse(text):
    if text == "":
        return ""
    return reverse(text[1:]) + text[0]

text = input("Enter a string: ")
print("Reversed string is:", reverse(text))

# 7. Program to find the sum of numbers from 1 to n using a for loop

n = int(input("Enter a number: "))

total_sum = 0

for i in range(1, n + 1):
    total_sum = total_sum + i

print("Sum of numbers is:", total_sum)

# 8. Program to count even numbers in a list

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

count = 0

for i in numbers:
    if i % 2 == 0:
        count = count + 1

print("Number of even numbers:", count)

# 9. Program to print all prime numbers between 1 and 100

for num in range(2, 101):

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)