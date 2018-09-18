stadsetning = 1
      
while stadsetning != 7:
    sanngildi = True  
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

    while sanngildi:
        breyting = str(input("Direction: ").lower())     
        if breyting == "n" and (stadsetning in (1, 4, 2, 8)):
            stadsetning += 1
        elif breyting == "s" and (stadsetning in (2, 5, 9, 3, 8)):
            stadsetning -= 1
        elif breyting == "w" and (stadsetning in (5, 9, 6)):
            stadsetning -= 3
        elif breyting == "e" and (stadsetning in (2, 3, 6)):
            stadsetning += 3
        else: 
            print("Not a valid direction!")
            continue
        sanngildi = False
    
else:
    print("Victory!")
    exit()
            