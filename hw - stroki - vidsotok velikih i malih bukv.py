def vids(n):
    v,m=0,0
    for i in n:
        if i.isupper():
            v+=1
        elif i.islower():
            m+=1
    return 'V',v,'m',m
print(vids('qweR'))
