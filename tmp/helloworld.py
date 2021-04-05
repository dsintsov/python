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
"""
##################
import random
mas=[random.randint(0,100) for i in range(20)]
print(mas)
for i in range(1,len(mas)-1):
    if mas[i-1] < mas[i] > mas[i+1]:
        print(i, end=" ")
#test1#################
