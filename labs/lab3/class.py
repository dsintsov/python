"""
Вариант 1	Создать класс – Треугольник, заданного тремя точками.
Функции-члены изменяют точки, обеспечивают вывод на экран координат, рассчитывают длины сторон и периметр треугольника.
Создать список объектов.
a)	подсчитать количество треугольников разного типа (равносторонний,	равнобедренный,	прямоугольный, произвольный).
b)	определить для каждой группы наибольший и наименьший по периметру объект.
"""

import math

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = x1, y1, x2, y2, x3, y3
        self.ab = self.ac = self.bc = -1
        self.isEquilateral = self.isIsosceles = self.isRectangular = False
        self.Perimeter = -1
        self.GetEdges()
        self.GetPerimeter()
        self.GetType()

    def GetCoordinats(self):
        return [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3]

    def GetEdges(self):
        self.ab = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.ac = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        self.bc = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)

    def GetPerimeter(self):
        self.Perimeter = self.ab + self.ac + self.bc

    def GetType(self):
        if self.ab == self.ac and self.ab == self.bc:
            self.isEquilateral = True
        if self.ab == self.ac or self.ab == self.bc or self.ac == self.bc:
            self.isIsosceles = True
        if self.ab ** 2 == self.ac ** 2 + self.bc ** 2 or self.ac ** 2 == self.ab ** 2 + self.bc or self.bc ** 2 == self.ac ** 2 + self.ab ** 2:
            self.isRectangular = True

TR = []
TR.append(Triangle(5, 4, 3, -1, 4, 5))
TR.append(Triangle(1, 3, -2, 0, -1, 4))
TR.append(Triangle(4, 1, -2, 3, -1, 4))
TR.append(Triangle(8, 13, 4, 0, 2, 11))

Equilateral = isIsosceles = isRectangular = 0
maxPerimeter=minPerimeter=TR[0].Perimeter
for T in TR:
    print("Coord =", T.GetCoordinats())
    print("Edges =", T.ab, T.ac, T.bc)
    print("Perimeter =", T.Perimeter)

    if T.isEquilateral:
        Equilateral+=1
    if T.isIsosceles:
        Isoscelesl += 1
    if T.isRectangular:
        Rectangular += 1

    if T.Perimeter > maxPerimeter:
        maxPerimeter= T.Perimeter
    if T.Perimeter < minPerimeter:
        minPerimeter= T.Perimeter

print("maxPerimeter=" + str(maxPerimeter), "minPerimeter=" + str(minPerimeter))