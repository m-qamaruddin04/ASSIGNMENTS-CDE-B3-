#10. Write a Python program to print the first 6 terms of a geometric sequence starting 
#with 2 and having a common ratio of 3. 
#The program should output the following sequence: 
#2 6 18 54 162 486 

# Program to print first 6 terms of a geometric sequence
# Starting with 2, common ratio = 3

start = 2       # First term
ratio = 3       # Common ratio
terms = 6       # Number of terms

print("The first 6 terms of the geometric sequence are:")

for i in range(terms):
    term = start * (ratio ** i)
    print(term, end=" ")
