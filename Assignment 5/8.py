#8. Write a program that prompts the user to input a number and prints its multiplication 
#table. 

# Program to print multiplication table of a number

num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}:")

for i in range(1, 11):   # Table up to 10
    print(f"{num} x {i} = {num * i}")
