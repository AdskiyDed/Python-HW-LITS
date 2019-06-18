n=0
n1=1
for i in range (1,1000,n1):
    n,n1=n1,n+n1
    if n>1000:
        break
    print(n1) 
