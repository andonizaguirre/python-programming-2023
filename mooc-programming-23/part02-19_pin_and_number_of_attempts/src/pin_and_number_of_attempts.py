# Write your solution here
count = 0
while True:
    pin = input("PIN")    
    count = count + 1
    if pin == "4321":
        break           
    print("Wrong")
if count == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {count} attempts")
