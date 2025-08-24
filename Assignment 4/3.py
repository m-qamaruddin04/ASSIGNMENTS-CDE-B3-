# 3. Find and display the largest number of a list without using built-in function max(). Your program 
#should ask the user to input values in list from keyboard. 

# Take input from user
user_input = input("Enter numbers separated by space: ")

# Convert input string into list of integers
lst = [int(x) for x in user_input.split()]

# Assume first element is the largest
largest = lst[0]

# Compare with rest of the elements
for num in lst:
    if num > largest:
        largest = num

print("The largest number is:", largest)
