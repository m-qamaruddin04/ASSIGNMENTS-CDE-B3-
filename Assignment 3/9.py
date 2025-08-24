# 9. Write a program in python that accepts a string to setup a passwords. Your entered password must 
#meet the following requirements: 
#The password must be at least eight characters long. 
#It must contain at least one uppercase letter. 
#It must contain at least one lowercase letter. 
#It must contain at least one numeric digit. 
#Your program should should perform this validation.

# Take password input
password = input("Set your password: ")

# Initialize conditions
has_upper = has_lower = has_digit = False

# Check each character
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True

# Validate conditions
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("✅ Password is valid.")
else:
    print("❌ Password is invalid. It must be at least 8 characters, "
          "contain uppercase, lowercase, and a digit.")
