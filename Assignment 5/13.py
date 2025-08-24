#13. Write a program that prompts the user to enter a number and repeats this process 5 
#times. The program should accumulate the numbers entered and then display the final 
#running total. 
#Sample Output: 
#Enter a number: 10 
#Enter a number: 15 
#Enter a number: 35 
#Enter a number: 40 
#Enter a number: 50 
#The final running total is: 150 

# Program to accumulate 5 numbers and display the final total

total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    total += num

print("The final running total is:", total)
