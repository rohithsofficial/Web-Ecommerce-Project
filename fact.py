n=int(input("Number 69"))
r = 1
for i in range(2,n):
    if n%i==0:
        r=0
    
if r==1:
    print("prime")
else:
    print("compo")