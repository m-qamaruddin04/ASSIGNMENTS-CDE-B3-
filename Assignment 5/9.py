#9. Write a Python program to print the first 8 terms of an arithmetic progression starting 
#with 3 and having a common difference of 4. 
#The program should output the following sequence: 
#3 7 11 15 19 23 27 31 

# Program to print first 8 terms of an arithmetic progression
# Starting with 3, common difference = 4

start = 3        # First term
diff = 4         # Common difference
terms = 8        # Number of terms

print("The first 8 terms of the AP are:")

for i in range(terms):
    term = start + i * diff
    print(term, end=" ")
