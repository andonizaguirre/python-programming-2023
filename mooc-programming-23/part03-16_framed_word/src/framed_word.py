# Write your solution here
string = input("Word:")
print("*" * 30)
spaces_start = (30 - 2 - len(string)) // 2 
spaces_end = spaces_start
if len(string) % 2 != 0:
    spaces_end = spaces_end + 1
print("*" + " " * spaces_start + string + " " * spaces_end + "*")
print("*" * 30)
