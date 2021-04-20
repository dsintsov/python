# Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах).

in_F = 'INPUT.txt'
out_F = 'OUTPUT.txt'

inputFile = open(in_F, 'rb')
outputFile = open(out_F, 'wb')
IN_SIZE = OUT_SIZE = 0

flag = False
for line in inputFile:
    IN_SIZE += len(line)
    if flag:
        outputFile.write(line)
        OUT_SIZE += len(line)
    flag = not flag

inputFile.close()
outputFile.close()

print("Size of " + in_F + " is " + str(IN_SIZE) + " byte")
print("Size of " + out_F + " is " + str(OUT_SIZE) + " byte")
