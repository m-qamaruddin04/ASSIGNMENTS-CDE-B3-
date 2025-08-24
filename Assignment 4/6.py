#6. Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It 
#should print the date in the form March 12, 2021.

# Dictionary to map month numbers to names
months = {
    "01": "January", "02": "February", "03": "March",
    "04": "April",   "05": "May",      "06": "June",
    "07": "July",    "08": "August",   "09": "September",
    "10": "October", "11": "November", "12": "December"
}

# Input date from user
date = input("Enter date in mm/dd/yyyy format: ")

# Split the date
mm, dd, yyyy = date.split("/")

# Print in required format
print(f"{months[mm]} {int(dd)}, {yyyy}")
