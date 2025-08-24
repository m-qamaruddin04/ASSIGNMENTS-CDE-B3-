#11. Write a program that asks the user for a positive integer value. The program should 
#calculate the sum of all the integers from 1 up to the number entered. For example, if 
#the user enters 20, the loop will find the sum of 1, 2, 3, 4, ... 20. 

# Program to calculate sum from 1 to n

n = int(input("Enter a positive integer: "))

# Initialize sum
total = 0

# Loop from 1 to n
for i in range(1, n + 1):
    total += i

print(f"The sum of integers from 1 to {n} is: {total}")
