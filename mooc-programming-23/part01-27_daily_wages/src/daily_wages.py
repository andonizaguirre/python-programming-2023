# Write your solution here
wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")
if day == "Sunday":
    wage = wage * 2
wages = wage * hours
print(f"Daily wages: {wages} euros")
