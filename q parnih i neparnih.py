s=input()
par, nepar = 0,0
for i in range (len(s)):
    if (int(s[i])%2)==0:
        par+=1
    else:
        nepar+=1
print('par',par,'nepar',nepar)

