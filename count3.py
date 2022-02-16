i=1
number=int(input("Enter a number:"))
#times table of whatever value is entered
print("The times table of",number,"is:")
while i<=10:
	print(number,"x",i,"=",(i*number))
	i=i+1
else:
	print("done!")