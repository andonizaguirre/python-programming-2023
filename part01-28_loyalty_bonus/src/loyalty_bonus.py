# Fix the program
points = int(input("How many points are on your card? "))
# python doesn't have block scope, this initialization is not needed
bonus = 1.1
if points < 100:
    bonus = 1.1
    print("Your bonus is 10 %")    
if points >= 100:
    bonus = 1.15
    print("Your bonus is 15 %") 
points *= bonus
print("You now have", points, "points")
