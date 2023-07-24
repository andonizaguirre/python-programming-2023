# Write your solution here
def squared(string, integer):
    length = integer
    row = ""
    while length > 0:
        row = row[integer:]
        while len(row) <= integer:
            row = row + string
        print(row[:integer])
        length -= 1

# def squared(characters, size):
#     i = 0
#     row = ""
#     while i < size * size:
#         if i > 0 and i % size == 0:
#             print(row)
#             row = ""
#         row += characters[i % len(characters)]
#         i += 1
#     print(row)

# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)
