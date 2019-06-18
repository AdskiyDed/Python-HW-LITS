def dec(s):
    def inner():
        print('\n', s(), '\n')
    return inner
@dec
def smart_input():
    s = input()
    d = s.split(' ')
    max1 = 0
    for i in d:
        i = int(i)
        if i > max1:
            max1 = i
    return max1
smart_input()