x,y,a,s,b=0,0,0,0,0
while True:
    b=input('start? y/n: ')
    if b=='y':
        x=int(input('enter 1 digit: '))
        y=int(input('enter 2 digit: '))
        a=input('deistvie +-*/:')
        if a is not ('+','-','*','/'):
            print('deistvie nevernoe')
            continue
        if a=='+':
            s=x+y
        elif a=='-':
            s=x-y
        elif a=='*':
            s=x*y
        elif a=='/':
            if y==0:
                print('delenia na nol, zadaite drugoe chislo')
                continue
            s=x/y
        print (s)
    else:
        break
print('vsem spasibo')

