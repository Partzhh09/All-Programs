amount=int(input("Enter Amount:"))
if amount<1000:
    discount=amount*0.05
    print("Discount",discount)
elif amount<5000:
    discount=amount*0.10
    print("Discount",discount)
else:
    discount=amount*0.15
    print("Discount",discount)
print("Net payable:",amount-discount)