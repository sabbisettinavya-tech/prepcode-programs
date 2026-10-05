blocked = ["admin","guest","root"]
username = input()
if username not in blocked:
    print("username allowed")
else:
    print("username blocked")