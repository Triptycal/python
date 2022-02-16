bill=int(input("Enter your bill:"))
paid=int(input("Enter paid amount:"))
num=paid-bill
if num>=50:
    fifties=int(num/50)
    print("£50's needed:",fifties)
    num=num-(fifties*50)
if num>=20:
    twenties=int(num/20)
    print("£20's needed:",twenties)
    num=num-(twenties*20)
if num>=10:
    tens=int(num/10)
    print("£10's needed:",tens)
    num=num-(tens*10)
if num>=5:
    fives=int(num/5)
    print("£5's needed:",fives)
    num=num-(fives*5)
if num>=2:
    two=int(num/2)
    print("£2's needed:",two)
    num=num-(two*2)
if num>=1:
    one=int(num/1)
    print("£1's needed:",one)
    num=num-(one*1)
else:
    print("done")


