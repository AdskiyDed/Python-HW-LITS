def slov(n):
    n=''.join([i for i in n if i not in(',','!')])# убирает символы (, ! ) в строке
    a=n.split(' ') # делит строку на елементы основываясь на пробеле
    d={}
    d2={}
    for i in a:
        q=0
        for k in a:
            if i==k:
                q+=1
                d2={k:q}
        d.update(d2)
    return d
print(slov('alfa, omega! betta ! hamma hamma'))