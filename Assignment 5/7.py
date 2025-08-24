# 7. Write a program that takes a number n as input from the user and generates the first 
#n terms of the series formed by squaring the natural numbers. 
#Sample output 
#Enter a number: 6 
#The first 6 terms of the series are: 
#1 4 9 16 25 36 

# Program to generate first n terms of square series

n = int(input("Enter a number: "))

print("The first", n, "terms of the series are:")

for i in range(1, n + 1):
    print(i * i, end=" ")
