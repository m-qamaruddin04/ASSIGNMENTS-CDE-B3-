#8. Write a program that display following output: 
#SHIFT 
#HIFTS 
#IFTSH 
#FTSHI 
#TSHIF 
#SHIFT 

# Original string
text = "SHIFT"

# Print rotated versions
for i in range(len(text) + 1):   # +1 to repeat the first word at the end
    rotated = text[i:] + text[:i]
    print(rotated)
