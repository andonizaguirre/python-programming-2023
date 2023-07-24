# Write your solution here
string = input("Please type in a string:")
last_index = 1
while last_index <= len(string):
    print(string[0:last_index])
    last_index = last_index + 1
