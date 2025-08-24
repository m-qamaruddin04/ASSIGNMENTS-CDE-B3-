#15. Write a Python program that prompts the user to enter a base number and an 
#exponent, and then calculates the power of the base to the exponent. The program 
#should not use the exponentiation operator (**) or the math.pow() function. The 
#program should handle both positive and negative exponents.

# Program to calculate power without using ** or math.pow()

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1

# Handle positive exponent
if exponent > 0:
    for i in range(exponent):
        result *= base
# Handle negative exponent
elif exponent < 0:
    for i in range(-exponent):
        result *= base
    result = 1 / result
# Exponent is 0
else:
    result = 1

print(f"{base} raised to the power {exponent} is: {result}")# Program to calculate power without using ** or math.pow()

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1

# Handle positive exponent
if exponent > 0:
    for i in range(exponent):
        result *= base
# Handle negative exponent
elif exponent < 0:
    for i in range(-exponent):
        result *= base
    result = 1 / result
# Exponent is 0
else:
    result = 1

print(f"{base} raised to the power {exponent} is: {result}")
