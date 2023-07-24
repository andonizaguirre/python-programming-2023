# Write your solution here
firstWord = input("Please type in the 1st word")
secondWord = input("Please type in the 2nd word")
if firstWord > secondWord:
    print(f"{firstWord} comes alphabetically last.")
elif secondWord > firstWord:
    print(f"{secondWord} comes alphabetically last.")
else:
    print("You gave the same word twice.")
