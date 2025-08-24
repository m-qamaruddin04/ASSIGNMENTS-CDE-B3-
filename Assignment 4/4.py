# 4. Write a program that rotates the element of a list so that the element at the first index moves to the 
#second index, the element in the second index moves to the third index, etc., and the element in the last 
#index moves to the first index.

# Take input from user
user_input = input("Enter list elements separated by space: ")

# Convert input string into list
lst = user_input.split()

print("Original List:", lst)

# Rotate the list
rotated_list = lst[1:] + [lst[0]]

print("Rotated List:", rotated_list)
