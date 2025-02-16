#1:Выводим квадратных число с точностью и округляем
def s_g(n, precision):
    for x in range(1, n+1):
        yield round(x**2, precision)
g = s_g(int(input("n = ")), 3)
for i in g:
 print(i)
 
#2:Выводим четные число с запятой
def e_n(n):
    for x in range(0, n+1, 2):
        yield x
n = int(input("N = "))
print(",".join(map(str, e_n(n))))

#3:Выводим число который кратные 3 и 4ж
def m_3_b_4(n):
    for i in range(0, n+1, 12):
        yield i
x = int(input("X = "))
for i in m_3_b_4(x):
    print(i)
    
#4:Выводим квадрата всех чисел от а до б:
def squares(a, n):
    for i in range(a, n+1):
        yield i ** 2
a = int(input())
n = int(input())
for x in squares(a,n):
    print(x)

#5: Выводим  от н до 0:
def gene(n):
    for i in range(n,-1,-1):
        yield i
n = int(input())
for x in gene(n):
    print(x)