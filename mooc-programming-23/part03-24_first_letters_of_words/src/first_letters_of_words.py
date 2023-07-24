# Write your solution here
string = input("Please type in a sentence:")
index = 0
print(string[index])
while index < len(string):
    if string[index] == " ":
        print(string[index + 1])
    index += 1
