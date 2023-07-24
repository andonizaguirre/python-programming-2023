# Write your solution here
number = int(input("Please type in a number:"))
step = 1
while step <= number:
    if step + 1 <= number:
        print(step + 1)
    print(step)
    step += 2
