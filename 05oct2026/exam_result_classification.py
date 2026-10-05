m1=int(input())
m2=int(input())
m3=int(input())
average=(m1+m2+m3)/3
if m1>=50 and m2>=50 and m3>=50:
    print("pass")
    if average>=75:
        print ("distinction")
else:
    print("fail")