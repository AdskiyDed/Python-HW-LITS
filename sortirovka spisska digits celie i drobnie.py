# def mas(*args):
q=int(2)
a=''
a1=[]
ac=[]
ad=[]
b={}
for i in range(q): #vodim stroki cherez slovar
    b.update({i:input(' ')})
for i in range (q): #formiruem spilknsok a1
    a=(b.get(i)).split(' ')
    for i in range(len(a)):
        a1.append(a[i])
for i in range(len(a1)): #perevodim str v digit
    a1[i]=float(a1[i])
for i in range(len(a1)): #formiruem spisok celih i drobnih
    if (a1[i]/int(a1[i]))!=1:
        ad.append(a1[i])
    elif (a1[i]/int(a1[i]))==1:
        ac.append(int(a1[i]))
    else:
        pass
ac.sort() #sortirovka
ad.sort()
for i in range(len(ad)): #skladivaem stroki
    ac.append(ad[i])
# print(ac)
# print(ad)
print(a)
# print(float(q))