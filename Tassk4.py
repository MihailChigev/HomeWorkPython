# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no


n = int(input("введите n - "))
m = int(input("введите m - "))
k = int(input("введите k - "))
if n*m > k:
    if k % n == 0 or k % m == 0:
        print(n, m, k,' -> yes')
    else:
        print(n, m, k,' -> no')
else:
    print(n, m, k,' -> no')