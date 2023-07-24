# Write your solution here
upper_limit = int(input("Upper limit:"))
base = int(input("Base:"))
power = 0
while base ** power <= upper_limit:
    print(base ** power)
    power = power + 1
