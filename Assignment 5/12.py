#12. write a program that takes a positive integer N as input and calculates the sum of 
#the reciprocals of all numbers from 1 up to N. The program should display the final sum. 
#Output of the program should be like: 
#Enter a positive integer: 5 
#The sum of reciprocals from 1 to 5 is: 2.28 

# Program to calculate sum of reciprocals from 1 to N

N = int(input("Enter a positive integer: "))

# Initialize sum
reciprocal_sum = 0

# Loop through 1 to N
for i in range(1, N + 1):
    reciprocal_sum += 1 / i

# Display result rounded to 2 decimal places
print(f"The sum of reciprocals from 1 to {N} is: {reciprocal_sum:.2f}")
