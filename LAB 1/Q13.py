#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
String = input("Enter a string: ")
swapped = ""

for char in String:
    if char.islower():
        swapped += char.upper()
    elif char.isupper():
        swapped += char.lower()
    else:
        swapped += char

print(swapped)
# we can also use .swapcase()