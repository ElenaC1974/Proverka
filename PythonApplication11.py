# -*- coding: cp1251 -*-
n=int(input("Введите количество чисел "))
a=0
for i in range(1, n+1):
 b=int(input("введите целое число "))
if b==0:
 a+=1
print(a)
