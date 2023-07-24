# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
total = 0
positives = 0
while True:
    number = int(input("Number:"))
    if number == 0:
        break
    count = count + 1
    total = total + number
    if number > 0:
        positives = positives + 1    
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {count - positives}")
