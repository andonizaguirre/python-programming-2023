# Write your solution here
number = int(input("Please type in a number:"))
start = 1
end = number
while start < end:
    print(start)
    print(end)
    start += 1
    end -= 1 
if start == end:
    print(start)
