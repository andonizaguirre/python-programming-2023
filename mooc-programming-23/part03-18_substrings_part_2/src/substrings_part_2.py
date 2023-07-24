# Write your solution here
string = input("Please type in a string:")
first_index = -1
while first_index >= -len(string): # Reverse indexing -> first index = -len(string)
    print(string[first_index:len(string)])
    first_index = first_index - 1

# start = len(string) - 1
# while start >= 0:
#     print(string[start:len(string)])
#     start -= 1
