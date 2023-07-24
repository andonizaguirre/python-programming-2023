# Write your solution here
upper_limit = int(input("Upper limit:"))
power = 0
while 2 ** power <= upper_limit:
    print(2 ** power)
    power = power + 1
