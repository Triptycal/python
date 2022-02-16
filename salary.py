salary=input("Enter your salary")
if int(salary)>=2000:
	tax=int(salary)*20/100
	net=int(salary)-tax
elif int(salary)<2000:
	tax=int(salary)*10/100
	net=int(salary)-tax
print("Tax:",tax)
print("Ner Salary:",net)