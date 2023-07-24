# Write your solution here
word = input("Please type in a word:")
character = input("Please type in a character:")
first_index = word.find(character) 
if first_index >= 0 and first_index + 3 <= len(word):
    print(word[first_index:first_index + 3])
