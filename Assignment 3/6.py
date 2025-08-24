#6. Write a program that asks the user to input his name and print its initials. Assuming that the user 
#always types first name, middle name and last name and does not include any unnecessary spaces. 
#For example, if the user enters Ajay Kumar Garg the program should display A. K. G. 
#Note:Don't use split() method 
# Take input from user

name = input("Enter your full name (First Middle Last): ")

print("Initials:", end=" ")

# First letter is always an initial
print(name[0].upper() + ".", end=" ")

# Traverse string to find spaces and pick next letter
for i in range(len(name)):
    if name[i] == " " and i+1 < len(name):
        print(name[i+1].upper() + ".", end=" ")