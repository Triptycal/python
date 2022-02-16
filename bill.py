quantity=90
price=8.50
bill=quantity*price
vat=bill*20/100
print("Quantity:",quantity)
print("Unit Price:",price)
print("--------------------")
print("Your bill is £",bill)
print("Your have to pay: £",vat,"as vat")
print("Your total bill is: £",(bill+vat))
print("--------------------")