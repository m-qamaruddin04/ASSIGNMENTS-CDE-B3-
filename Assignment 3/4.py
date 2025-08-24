#4. Write a Python program that accepts a string from user. Your program should create a new string in 
#reverse of first string and display it. 
#For example if the user enters the string 'EXAM' then new string would be 'MAXE' 
# Take input from user

text = input("Enter a string: ")

# Reverse the string using slicing
reversed_text = text[::-1]

# Display result
print("Reversed string:", reversed_text)
