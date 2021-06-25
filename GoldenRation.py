import function
import math

def goldenRatio(epsilon, a, b):
    prev = b - a
    countIter = 1
    countFunc = 0
    phi = (math.sqrt(5) + 1) / 2
    resphi = 2 - phi
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    f1 = function.func(x1)
    f2 = function.func(x2)
    countFunc += 2
    while (b - a) > epsilon:
        countIter += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + resphi * (b - a)
            f1 = function.func(x1)
            countFunc += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - resphi * (b - a)
            f2 = function.func(x2)
            countFunc += 1
        curent = b - a
        print(curent / prev)
        prev = curent
    print("минимум: ", (x1 + x2) / 2, "количество итераций: ", countIter, "количество вызовов функций: ", countFunc)