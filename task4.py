#Вариант 3

def C (m, n):
    if n == 0:
        return 1
    elif n > n:
        return 0
    else:
        return C(m - 1, n) + C(m - 1, n - 1)





m, n2 = map(int, input().split())
print(C(m, n))
