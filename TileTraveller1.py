
stadsetning = 1
rett_val = ""

while stadsetning != 7:
    if stadsetning == 1 or stadsetning == 4:
        print("You can travel: (N)orth")
        breyting = str(input("Direction: ").lower())
        if breyting != "n":
            print("Not a valid direction")
            continue
    elif stadsetning == 2:
        print("You can travel: (N)orth or (S)outh or (E)ast.")
        breyting = str(input("Direction: ").lower())
        if breyting != "n" and breyting != "s" and breyting != "e":
            print("Not a valid direction")
            continue
    elif stadsetning == 5 or stadsetning == 9:
        print("You can travel: (S)outh or (W)est.")
        breyting = str(input("Direction: ").lower())
        if breyting != "s" and breyting != "w":
            print("Not a valid direction")
            continue
    elif stadsetning == 3:
        print("You can travel: (S)outh or (E)ast.")
        breyting = str(input("Direction: ").lower())
        if breyting != "s" and breyting != "e":
            print("Not a valid direction")
            continue
    elif stadsetning == 6:
        print("You can travel: (E)ast or (W)est.")
        breyting = str(input("Direction: ").lower())
        if breyting != "e" and breyting != "w":
            print("Not a valid direction")
            continue
    elif stadsetning == 8:
        print("You can travel: (N)orth or (S)outh.")
        breyting = str(input("Direction: ").lower())
        if breyting != "n" and breyting != "s":
            print("Not a valid direction")
            continue

    if breyting == "n":
        stadsetning += 1
    elif breyting == "s":
        stadsetning -= 1
    elif breyting == "w":
        stadsetning -= 3
    elif breyting == "e":
        stadsetning += 3
else:
    print("Victory!")
            