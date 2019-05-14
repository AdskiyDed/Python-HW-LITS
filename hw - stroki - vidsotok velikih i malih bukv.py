def vids(n):
    v,m=0,0
    p=len(n)
    for i in n:
        if i.isupper:
            v+=1
    return 'dov',p,'vel', v/p,'mal',(p-v)/p
print(vids(input()))
