#1. Write a program that accepts a list from user and print the alternate element of list. 

# Accept list input from user
user_input = input("Enter elements separated by space: ")

# Convert input string to list
lst = user_input.split()

# Print alternate elements (0, 2, 4, ...)
print("Alternate elements are:")
for i in range(0, len(lst), 2):
    print(lst[i])
