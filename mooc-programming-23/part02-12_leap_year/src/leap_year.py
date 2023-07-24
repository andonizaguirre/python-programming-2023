# Write your solution here
year = int(input("Please type in a year:"))
# Any year divisible by 400 is divisible by both 4 and 100
if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# First, we make assumption that a year is not a leap year
# leap_year = False
# if year % 100 == 0:
#     if year % 400 == 0:
#         leap_year = True
# elif year % 4 == 0:
#     leap_year = True
# if leap_year:
#     print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")
