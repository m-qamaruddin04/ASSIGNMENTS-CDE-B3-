#1. Write a program that accepts a string from user. Your program should count and display number of vowels in that string. 

# Take input from user
text = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for ch in text:
    if ch in vowels:
        count += 1

# Print result
print("Number of vowels in the string:", count)
