#5. Write a Python program that accepts a string from user. Your program should create a new string by 
#shifting one position to left. 
#For example if the user enters the string 'examination 2021' then new string would be 'xamination 
#2021e' 
# Take input from user

text = input("Enter a string: ")

# Check if string has at least 1 character
if len(text) > 0:
    shifted_text = text[1:] + text[0]
else:
    shifted_text = text  # empty string stays empty

# Display result
print("New string:", shifted_text)
