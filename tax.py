def tax(s):
	T=s*20/100
	return T

salary=int(input("Enter your salary:"))
netsalary=salary-tax(salary)
print("Tax:",tax(salary))
print("Net",netsalary)