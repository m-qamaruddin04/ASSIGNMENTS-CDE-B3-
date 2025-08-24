#5. Write a program that input a string and ask user to delete a given word from a string.

# Input string from user
text = input("Enter a string: ")

# Word to delete
word_to_delete = input("Enter the word you want to delete: ")

# Remove word
new_text = text.replace(word_to_delete, "")

print("String after deletion:", new_text.strip())
