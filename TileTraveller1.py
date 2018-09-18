
x = 1
y = 1
stadsetning = (x, y)
rett_val = ""

while stadsetning != 9:
    if stadsetning == (1,1) or (2,1):
        print("You can travel (N)orth")
        breyting = str(input("Direction: ").lower())
        rett_val = "n"
    elif stadsetning == (1,2):
        print("You can travel (N)orth or (S)outh or (W)est.")
        breyting = str(input("Direction: ").lower())
        rett_val = "n" or "s" or "w"
    elif stadsetning == (2,2) or (3,3):
        print("You can travel (S)outh or (W)est.")
        breyting = str(input("Direction: ").lower())
        rett_val = "s" or "w"
    elif stadsetning == (1,3):
        print("You can travel (S)outh or (E)ast.")
        breyting = str(input("Direction: ").lower())
        rett_val = "s" or "e"
    elif stadsetning == (2,3):
        print("You can travel (E)ast or (W)est.")
        breyting = str(input("Direction: ").lower())
        rett_val = "e" or "w"
    elif stadsetning == (3,2):
        print("You can travel (N)orth or (S)outh.")
        breyting = str(input("Direction: ").lower())
        rett_val = "n" or "s"

    if breyting == rett_val:
        if breyting == "n":
            y += 1
        elif breyting == "s":
            y -= 1
        elif breyting == "w":
            x -= 1
        elif breakpoint == "e":
            x += 1
            