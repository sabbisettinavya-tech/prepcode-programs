price=int(input())
discount=int(input())
extra=int(input())
price-=price*discount/100
price-=extra
price("final price:",price)