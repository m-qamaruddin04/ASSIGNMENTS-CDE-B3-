#7. A palindrome is a string that reads the same backward as forward. For example, the words dad, 
#madam and radar are all palindromes. Write a programs that determines whether the string is a 
#palindrome. 
#Note: do not use reverse() method 
# Take input from user

text = input("Enter a string: ")

# Assume it's a palindrome
is_palindrome = True

# Compare characters from both ends
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

# Display result
if is_palindrome:
    print(text, "is a Palindrome ✅")
else:
    print(text, "is NOT a Palindrome ❌")