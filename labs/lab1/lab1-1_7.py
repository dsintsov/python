# № 7: В переменную Y ввести номер года. Определить, является ли год високосным.
"""
wiki: год, номер которого кратен 400, — високосный;
остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
остальные годы, номер которых кратен 4, — високосные
"""

# Checking the user input
while True:
    Y = input("Enter a year: ")
    try:
        if int(Y) > 0:
            break  # input is INT and greater than 0
        else:
            raise TypeError()  # just call an exception
    except:
        print("ERR: \"{0}\" - it\'s NOT a valid year number, try again!".format(str(Y)))

Y = int(Y)

print(str(Y), end='')
if Y % 400 == 0 or Y % 4 == 0 and Y % 100 != 0:
    print(" - is a leap year")
else:
    print(" - isn't a leap year")

exit(0)
