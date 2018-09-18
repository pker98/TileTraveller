# Git Repo: https://github.com/pker98/TileTraveller
# Algorithm/Hugsun á bakvið forritið
# * Hugsa sem tölur frá 1 - 9 frekar en x og y hnit
# * Hugsa hvernig N, S, W, E breyta tölunni 
# * Búa til sem minnstan kóða með því að prófa mig áfram
# * Helst reyna aldrei að endurtaka neinn kóða

def leidbeiningar(stadsetning):
    if stadsetning == 1 or stadsetning == 4:
        return print("You can travel: (N)orth.")     
    elif stadsetning == 2:
        return print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif (stadsetning == 5 or stadsetning == 9):
        return print("You can travel: (S)outh or (W)est.")
    elif stadsetning == 3:
        return print("You can travel: (E)ast or (S)outh.")
    elif stadsetning == 6:
        return print("You can travel: (E)ast or (W)est.")
    elif stadsetning == 8:
        return print("You can travel: (N)orth or (S)outh.")

def reikna_faerslu(breyting, stadsetning):
    if breyting == "n" and (stadsetning in (1, 4, 2, 8)):
        stadsetning += 1
    elif breyting == "s" and (stadsetning in (2, 5, 9, 3, 8)):  # Í þessum if-setningum er checkað hvort að stafurinn sé einn af NSWE og
        stadsetning -= 1                                        # hvort hann sé á stað sem má fara í þá átt sem slegin er inn
    elif breyting == "w" and (stadsetning in (5, 9, 6)):        
        stadsetning -= 3
    elif breyting == "e" and (stadsetning in (2, 3, 6)):
        stadsetning += 3
    return stadsetning

stadsetning = 1
      
while stadsetning != 7:
    sanngildi = True            # Notað fyrir seinni while lykkjuna
    leidbeiningar(stadsetning)
    while sanngildi:
        breyting = str(input("Direction: ").lower())
        gomul_stadsetning = stadsetning 
        stadsetning = reikna_faerslu(breyting, stadsetning)
        if stadsetning == gomul_stadsetning: 
            print("Not a valid direction!")
            continue
        sanngildi = False   # Ef að N/S/W/E er bara slegið inn þegar það má þá skilar þetta False og farið
                            # er úr while-lykkjunni, annars býður forritið um nýtt input þangað til það er slegið rétt inn
else:
    print("Victory!")
    exit()
            