#14. Write a program that prompts the user to enter a positive integer and calculates its 
#factorial. The factorial of a positive integer 'n' is denoted as 'n!' and is calculated by 
#multiplying all the integers from 1 to 'n' together. For example, the factorial of 5 
#(denoted as 5!) is calculated as 1 x 2 x 3 x 4 x 5. 
#The program should display the factorial value if the input is a positive number, or 
#display a message stating that the factorial does not exist for negative numbers. 
#Additionally, for an input of zero, the program should output that the factorial of 0 is 1. 

# Program to calculate factorial

n = int(input("Enter a positive integer: "))

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")
