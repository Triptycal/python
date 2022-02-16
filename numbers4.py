number=int(input("Enter a number:"))
if number>1000:
    print("A")
    if number>2000:
        print("C")
        if number>3000:
            print("H")
        print("M")
    else:
        print("D")
        if number>1500:
            print("J")
        else:
            print("I")
        print("L")
    print("N")
else:
    print("B")
    if number>500:
        print("E")
    else:
        print("F")
    print("K")
print("O")
print("P")