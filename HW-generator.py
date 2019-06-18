# def matrix(n):
#     return([[0 for i in range(n)] for x in range(n)])
# print(matrix(3))

#функция принимает число и выводит все простые числа меньше равные числу
def isprimes(i):
    if i==2:
        return True
    for n in range(2,i):
        if i%n==0:
            return False
    return True
def primes(i):
    return ([n for n in range(i) if isprimes(n)])
print(primes(100))