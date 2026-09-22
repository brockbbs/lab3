from math import *
def y(x):
  num1 = x * sin(2 * x) / cos(2 * x)
  num2 = x * log(x) / (sin(x) + cos(x))
  return num1 * num2

a = 0.1
b = 0.9
h = 0.05
n = round((b - a) / h) + 1

for i in range(n):
  x = a + i + h
  print(f"{x:8.2f} | {y(x):12.5f}")
