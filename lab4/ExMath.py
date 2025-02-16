#1: Преобразуем градус на радиан:
import math
d = int(input())
r = math.radians(d)
print(r)

#2: Вычисления площади трапеции:
def t_area(a, b, h):
    return (a+b)*h / 2
a = float(input())
b = float(input())
h = float(input())
area = t_area(a, b, h)
print(area)

#3:вычисления площади правильного многоугольника:
import math 
def r_poly_area(n, s):
    return (n * s**2) / (4*math.tan(math.pi/n))
n = float(input())
s = float(input())
area = r_poly_area(n, s)
print(int(area))

#4: для вычисления площади параллелограмма:
def p_area(a, h):
    return a * h
a = float(input())
h = float(input())
area = p_area(a, h)
print(area)