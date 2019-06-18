n=0
n1,n2=0,1
s=input()
for i in range (len(s)):
    n+=int(s[i])
    n1=int(s[i])
    if n1==0:
        n1=1
    n2*=n1
print('suma',n,'dobutok',n2)
