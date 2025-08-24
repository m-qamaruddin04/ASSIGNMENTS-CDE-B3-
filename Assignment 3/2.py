# 2. Write a program that reads a string from keyboard and display: 
# * The number of uppercase letters in the string 
# * The number of lowercase letters in the string 
# * The number of digits in the string 
# * The number of whitespace characters in the string 


# Take input from user
text = input("Enter a string: ")

# Initialize counters
upper = lower = digits = spaces = 0

# Check each character
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

# Display results
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
print("Number of digits:", digits)
print("Number of whitespace characters:", spaces)
