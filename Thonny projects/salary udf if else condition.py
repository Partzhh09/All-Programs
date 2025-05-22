salary=int(input("Enter your salary :"))
if salary<5000:
    bonus=salary+3000
    print("Bonus :",bonus)
if salary<=6000 & salary>=20000:
    bonus=salary+2000
    print("Bonus :",bonus)
else:
    bonus=salary+1000
    print("Bonus :",bonus)
print("Total salary is :",bonus)