# Write your solution here
firstLetter = input("1st letter:")
secondLetter = input("2nd letter:")
thirdLetter = input("3rd letter:")
if firstLetter > secondLetter and firstLetter > thirdLetter: # biggest = firstLetter
    if secondLetter > thirdLetter:
        middle = secondLetter
    else:
        middle = thirdLetter 
elif secondLetter > thirdLetter: # biggest = secondLetter
    if firstLetter > thirdLetter:
        middle = firstLetter
    else:
        middle = thirdLetter 
else: # biggest = thirdLetter
    if firstLetter > secondLetter:
        middle = firstLetter
    else:
        middle = secondLetter 
print("The letter in the middle is " + middle)
