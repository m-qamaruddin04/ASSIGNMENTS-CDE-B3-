# 7. Write a program with a function that accepts a string from keyboard and create a new string after 
#converting character of each word capitalized. For instance, if the sentence is "stop and smell the roses." 
#the output should be "Stop And Smell The Roses"

def capitalize_words(sentence):
    result = ""
    capitalize_next = True   # Flag to know when to capitalize
    
    for char in sentence:
        if capitalize_next and char.isalpha():   # Capitalize only letters
            result += char.upper()
            capitalize_next = False
        else:
            result += char.lower()
            if char == " ":   # Reset flag after space
                capitalize_next = True
    return result

# Input from user
text = input("Enter a sentence: ")
new_text = capitalize_words(text)
print("Capitalized Sentence:", new_text)
