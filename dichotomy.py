import function


def dichotomy(epsilon, a, b):
    countIter = 0
    countFunc = 0
    local_a = a
    local_b = b
    prev = b - a
    while (local_b - local_a) > epsilon:
        countIter += 1
        x1 = (local_a + local_b) / 2 - epsilon / 10
        x2 = (local_a + local_b) / 2 + epsilon / 10
        x1tmp = function.func(x1)
        x2tmp = function.func(x2)
        countFunc += 2
        if x1tmp > x2tmp:
            local_a = x1
        else:
            local_b = x2
        curent = local_b - local_a
        print(curent/prev)
        prev = curent
    print("минимум: ", (local_a + local_b) / 2, "количество итераций: ", countIter, "количество вызовов функций: ", countFunc)
