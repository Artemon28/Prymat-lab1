import math
import Brent
import dichotomy
import function
import GoldenRation
import Fibonacci
import Parabol

import array
import numpy
import matplotlib.pyplot as plt
import scipy as scipy

epsilon = 0.1
a = 6
b = 10
# print('Дихтомия')
# dichotomy.dichotomy(epsilon, a, b)
# print('Золотое сечение')
# GoldenRation.goldenRatio(epsilon, a, b)
print('Фибоначи')
Fibonacci.Fibonacci(epsilon, a, b)
# print('метод Парабол')
# print(Parabol.parabola(a, 7,  b, epsilon))
# print('Брент')
# print(Brent.Brent(epsilon, a, b))
