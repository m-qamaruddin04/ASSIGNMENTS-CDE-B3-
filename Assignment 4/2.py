#2. Write a program that accepts a list from user. Your program should reverse the content of list and 
#display it. Do not use reverse() method. 

# Accept list input from user
user_input = input("Enter elements separated by space: ")

# Convert input string to list
lst = user_input.split()

# Reverse list using slicing
reversed_list = lst[::-1]

print("Reversed list is:", reversed_list)
