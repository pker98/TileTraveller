
stadsetning = 1

while stadsetning != 7:
    if stadsetning == 1 or stadsetning == 4:
        print("You can travel: (N)orth.")     
    elif stadsetning == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif (stadsetning == 5 or stadsetning == 9):
        print("You can travel: (S)outh or (W)est.")
    elif stadsetning == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif stadsetning == 6:
        print("You can travel: (E)ast or (W)est.")
    elif stadsetning == 8:
        print("You can travel: (N)orth or (S)outh.")

    breyting = str(input("Direction: ").lower())
    
    if breyting == "n" and (stadsetning == 1 or 4 or 2 or 8):
        stadsetning += 1
    elif breyting == "s" and (stadsetning == 2 or 5 or 9 or 3 or 8):
        stadsetning -= 1
    elif breyting == "w" and (stadsetning == 5 or 9 or 6):
        stadsetning -= 3
    elif breyting == "e" and (stadsetning == 2 or 3 or 6):
        stadsetning += 3
    else: 
        print("Not a valid direction!")
    
else:
    print("Victory!")
    exit()
            