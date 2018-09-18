# Git Repo: https://github.com/pker98/TileTraveller
# Algorithm/Hugsun á bakvið forritið
# * Hugsa um tölur frá 1 - 9 frekar en x og y hnit
# * Hugsa hvernig N, S, W, E breyta tölunni 
# * Búa til sem minnstan kóða með því að prófa mig áfram
# * Helst reyna aldrei að endurtaka neinn kóða

stadsetning = 1
      
while stadsetning != 7:
    sanngildi = True            # Notað fyrir seinni while lykkjuna
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

    while sanngildi:                                                # Þessi while loopa á að keyra aðeins einu sinni, nema að notandi slær 
        breyting = str(input("Direction: ").lower())                # inn vitlaust þá keyrir hún aftur þangað til hann slær inn rétt    
        if breyting == "n" and (stadsetning in (1, 4, 2, 8)):
            stadsetning += 1
        elif breyting == "s" and (stadsetning in (2, 5, 9, 3, 8)):  # Í þessum if-setningum er checkað hvort að stafurinn sé einn af NSWE og
            stadsetning -= 1                                        # hvort hann sé á stað sem má fara í þá átt sem slegin er inn
        elif breyting == "w" and (stadsetning in (5, 9, 6)):        
            stadsetning -= 3
        elif breyting == "e" and (stadsetning in (2, 3, 6)):
            stadsetning += 3
        else: 
            print("Not a valid direction!")
            continue
        sanngildi = False   # Ef að N/S/W/E er bara slegið inn þegar það má þá skilar þetta False og farið
                            # er úr while-lykkjunni, annars býður forritið um nýtt input þangað til það er slegið rétt inn
else:
    print("Victory!")
    exit()
            