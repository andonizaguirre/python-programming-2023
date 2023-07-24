# Write your solution here
times = int(input("How many times a week do you at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
money = float(input("How much money do you spend on groceries in a week"))
weekly = money + times * price
print("Average food expenditure:")
print(f"Daily: {weekly / 7} euros")
print(f"Weekly: {weekly} euros")
