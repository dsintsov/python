"""
Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b на квадраты
с наибольшей возможной на каждом этапе стороной.
Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.
"""

COUNT=0
def SQUARE(a, b):
    global COUNT;
    if a>0 and b>0:
       COUNT+=1
       if a <= b:
           b-=a
           print(a)
       else:
           a-=b
           print(b)
       SQUARE(a, b)

def INT_INPUT():
    while True:
        Y = input()
        try:
            if int(Y) > 0:
                return Y# input is INT and greater than 0
            else:
                raise TypeError()  # just call an exception
        except:
            print("ERR: \"{0}\" - it\'s NOT a valid integer, try again!".format(str(Y)))

print("Enter the length of the first rectangle edge: ", end='')
A = int(INT_INPUT())
print("Enter the length of the second rectangle edge: ", end='')
B = int(INT_INPUT())

print("Edges:")
SQUARE(A,B)
print("There are "+str(COUNT)+" squares")

exit(0)