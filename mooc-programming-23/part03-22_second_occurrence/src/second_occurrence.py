# Write your solution here
string = input("Please type in a string:")
substring = input("Please type in a substring:")
index = string.find(substring)
if index >= 0:
    string_sliced = string[index + len(substring):]
    index = string_sliced.find(substring)
    index_compensated = index + len(string) - len(string_sliced) # Add the equivalent to the characters lost in the slice
if index >= 0:
    print(f"The second occurrence of the substring is at index {index_compensated}.")
else:
    print("The substring does not occur twice in the string.")

# index1 = string.find(substring)
# index2 = -1
# if index1 != -1:
#     string = string[index1+len(substring):]
#     index2 = string.find(substring)
# if index2 == -1:
#     print("The substring does not occur twice in the string.")
# else:
#     print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".")
