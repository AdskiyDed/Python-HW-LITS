#sortirovka bulbashkoi
# # a=[2,1,6,3,8,9,0,4,3,23,4,20,5,0]
# a=['raibow','train','alfa','1','alt']
# def sort_b(a):
#     for i in range (len(a)-1):
#         for k in range (len(a)-1):
#             if a[k]>a[k+1]:
#                 a[k],a[k+1]=a[k+1],a[k]
#     return a
# print(sort_b(a))

#sortirovka vstavkoi
a=[2,1,6,3,8,9,0,4,3,23,4,20,5,0,1]
for i in range (len(a)):
    n=i
    while n>=0:
        for k in range (1,i+1):
            if a[k]<a[k-1]:
                a[k],a[k-1]=a[k-1],a[k]
        n-=1
print(a)