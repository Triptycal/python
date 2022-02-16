salary=int(input("Enter your salary"))
if salary>=2000:
	tax=salary*25/100
elif salary>=1000:
    tax=salary*15/100
else:
	tax=0
net=salary-tax
print("Tax:",tax)
print("Net Salary:",net)