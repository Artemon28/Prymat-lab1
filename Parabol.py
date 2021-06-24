import function
import math


def parabola(x1, x2, x3, epsilon):
    f1 = function.func(x1)
    f2 = function.func(x2)
    f3 = function.func(x3)
    countFunc = 3
    iter = 1
    while 1:
        ucurrent = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / (
                    2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        fu = function.func(ucurrent)
        countFunc += 1
        if iter > 1 and math.fabs(uprev - ucurrent) < epsilon:
            print(ucurrent, fu)
            # itercount.append(iter)
            return ("Локальный минимум: ", ucurrent, "Количество итераций: ", iter, "Количество вычислений: ", countFunc)
        uprev = ucurrent
        if f2 > fu:
            if ucurrent > x2:
                x1 = x2
                f1 = f2
            else:
                x3 = x2
                f3 = f2
            x2 = ucurrent
            f2 = fu
        else:
            if ucurrent > x2:
                x3 = x2
                f3 = f2
            else:
                x1 = x2
                f1 = f2
        iter = iter + 1