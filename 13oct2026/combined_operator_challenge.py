price=1000
quantity=2
total=price*quantity
member=True
coupon=True
if member:
    total-=total*0.10
if coupon:
    total-=total*0.05
print("final bill:",total)