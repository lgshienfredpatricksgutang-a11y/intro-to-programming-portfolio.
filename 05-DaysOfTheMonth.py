# this program tells the number of days in a month based on user input

# Dictionary days in month program
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Get the month number from the user
month_num = int(input("Enter month number (1-12): "))

# Determine the number of days in the month
if month_num == 2:
    is_leap = input("Is it a leap year? (yes/no): ").lower()
    if is_leap == 'yes':
        print("29 days")
    else:
        print("28 days")
else:
    # Print the number of days for the given month
    print(f"{month_days[month_num]} days")
     
    # outputs the number of days in the month based on user input
