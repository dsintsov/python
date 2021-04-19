"""
a = int(input("Введите целое число:\n"))
if a % 2 == 0:
    print(str(a) + " -  четное число")
#elif :
else:
    print(str(a) + " -  нечетное число")
##################
import numpy
for x in numpy.arange(0, 0.6, 0.1):
    print(2 ** x)

##################
x = 1
y=2 ** x
while y < 100:
    print(y)
    x += 1
    y = 2 ** x

exit(0)
##################
import random
n = int(input("Введите размер списка:\n"))
A = []
for i in range(n):
    #    A.append(random.random()) # from 0 to 1
    A.append(random.randint(10, 100)) #
    print(A[i])
s=sum(A) # sum of all elements
l=len(A) # count of elements
print(s)

##################
import random
mas=[random.randint(0,100) for i in range(20)]
print(mas)
for i in range(1,len(mas)-1):
    if mas[i-1] < mas[i] > mas[i+1]:
        print(i, end=" ")
#test1#################
"""

import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a



def ins_sort(A):
    for i in range(1, len(A)):
        t = A[i]
        j = i
        while j >= 0:
            if A[j-1] > t:
                A[j] = A[j-1]
            else:
                break
            j -= 1
        A[j] = t

A = [9, 1, 15, 28, 6]
ins_sort(A)
print(A)



def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой"])
x=[]
y1=[]
y2=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)


    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()