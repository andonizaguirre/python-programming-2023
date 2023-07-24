# Write your solution here
word = input("Please type in a word:")
character = input("Please type in a character:")
while len(word) > 0:  
    first_index = word.find(character)  
    if first_index >= 0 and first_index + 3 <= len(word):
        print(word[first_index:first_index + 3])
    if first_index == -1: # Avoid infinite loop, first_index = -1 + 1 = 0
        first_index = 0
    word = word[first_index + 1:len(word)] 

# index = 0
# while index + 3 <= len(word):
#     if word[index] == character:
#         print(word[index:index+3])
#     index += 1
