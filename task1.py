from math import *
def y(x):
    numerator = math.exp(-2 * x) * math.pi * (x ** 2 + math.sqrt(x + 5))
    inner = abs(math.exp(x) - 2 * math.log(x))
    denominator = math.sqrt(abs(2 * x - math.sqrt(inner)))
    return numerator / denominator
x = 0.5
print(f"y({x}) = {y(x):.5f}")
