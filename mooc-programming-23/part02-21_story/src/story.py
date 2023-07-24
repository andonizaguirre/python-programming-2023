# Write your solution here
phrase = ""
last_word = ""
while True:    
    word = input("Please type in a word:")    
    if word == "end" or word == last_word :
        break    
    phrase = phrase + word + " "
    last_word = word
print(phrase)
