"""
Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
Размер списка n ввести с клавиатуры.
№7 Удалить из списка все элементы, совпадающие с его минимальным значением.
"""
import random

# Checking the user input
while True:
    n = input("Enter a list length: ")
    try:
        if int(n) > 0:
            break  # input is INT and greater 0
        else:
            raise TypeError()  # just call an exception
    except:
        print("ERR: \"{0}\" - it\'s NOT a valid list length, try again!".format(str(n)))

n = int(n)

A = []
# searching min element
MIN = 99
for i in range(n):
    A.append(random.randint(0, 99))
    if A[i] < MIN:
        MIN = A[i]
print("A =", A)
print("MIN = " + str(MIN))

# delete all elements which eq MIN
i = 0
while i < len(A):
    if A[i] == MIN:
        del A[i]
    else:
        i += 1
print("A =", A)

exit(0)
