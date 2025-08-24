#3. Write a Python program that accepts a string from user. Your program should create and display a 
#new string where the first and last characters have been exchanged. 
#For example if the user enters the string 'HELLO' then new string would be 'OELLH' 

# Take input from user
text = input("Enter a string: ")

# Check if string has at least 2 characters
if len(text) < 2:
    new_text = text  # no change for single char or empty string
else:
    new_text = text[-1] + text[1:-1] + text[0]

# Display result
print("New string:", new_text)
