# Write your solution here
limit = int(input("Limit:"))
total = 1
number = 1
numbers = str(number)
while total < limit:
    number = number + 1
    numbers = numbers + " + " + str(number)
    total = total + number    
print(f"The consecutive sum: {numbers} = {total}")
