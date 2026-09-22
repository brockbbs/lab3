from math import *
def y(x):
    num1 = exp(-2 * x) * (x ** 2 + sqrt(x + 5))
    num2 = abs(exp(x) - 2 * log(x))
    num3 = sqrt(abs(2 * x - sqrt(num2)))
    return num1 / num3
x = 0.5
print(f"y({x}) = {y(x):.5f}")
