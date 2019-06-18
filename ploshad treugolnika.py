import math
def distance(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        print ('eto treugolnik')
        print ('rahuvaty ploshad? y/n')
        r=input()
        if r=='y':
            p=(a+b+c)/2
            print('Ploshad =', end=' ')    
            return (math.sqrt(p*(p-a)+p*(p-b)+p*(p-c)))
        else:
            return
    else:
        return 'eto ne treugolnik'
print(distance(int(input()),int(input()),int(input())))