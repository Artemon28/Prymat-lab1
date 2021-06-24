import math
import array
import function

#
# def FibonacciFunc(n):
#     return 1 / math.sqrt(5) * pow(((1 + math.sqrt(5)) / 2), n) - pow(((1 - math.sqrt(5)) / 2), n)

Y = array.array('i', [])
X1 = array.array('i', [])
Y1 = array.array('d', [])

def Fibonacci(epsilon, a, b):
    countIter = 0
    countFunc = 0
    fib1 = 2
    fib2 = 1
    fib3 = 1
    while ((b - a) / epsilon) > fib1:
        fib3 = fib2
        temp_fib = fib1
        fib1 = fib2 + fib1
        fib2 = temp_fib
    tmp1 = a + fib3 / fib1 * (b - a)
    tmp2 = a + fib2 / fib1 * (b - a)
    count_operation = 0
    ytmp1 = function.func(tmp1)
    ytmp2 = function.func(tmp2)
    countFunc += 2
    while (b - a > epsilon):
        countIter += 1
        count_operation = count_operation + 1
        if (ytmp1 > ytmp2):
            a = tmp1
            tmp1 = tmp2
            ytmp1 = ytmp2
            tmp2 = a + fib2 / fib1 * (b - a)
            ytmp2 = function.func(tmp2)
            countFunc += 1
        else:
            b = tmp2
            tmp2 = tmp1
            ytmp2 = ytmp1
            tmp1 = a + fib3 / fib1 * (b - a)
            ytmp1 = function.func(tmp1)
            countFunc += 1
        fib3 = fib2
        tmp_fib = fib1
        fib1 = fib2 + fib1
        fib2 = tmp_fib
    tmp2 = tmp1 + epsilon
    ytmp2 = function.func(tmp2)
    countFunc += 1
    if (ytmp1 >= ytmp2):
        a = tmp1
    else:
        b = tmp2
    print("минимум: ", (a + b) / 2, "количество итераций: ", countIter, "количество вызовов функций: ", countFunc)