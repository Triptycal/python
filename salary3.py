salary=int(input("Enter your salary"))
if salary>=1000:
#will execute only if true
    if salary>=2000:
        tax=salary*25/100
    else:
        tax=salary*15/100
else:
#will execute only if false
	tax=0
net=salary-tax
print("Tax:",tax)
print("Net Salary:",net)