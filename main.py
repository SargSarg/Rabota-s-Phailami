myFile = open('filename.txt', 'rt', encoding="utf8") #encoding чтоб кириллицу прочесть
print(myFile.read())#открывает весь файл как одну строку а цифра означает первые символы

print(myFile.readline(3)) #открывает построчно а при повторном запуске выдает следующую строку

print(myFile.readlines(1)) #возвращает строку и если цифра больше кол-ва символов в 1 строке то выдаст следующую(ие)

for line in myFile: #тоже возвращает построчно а не как всё одной строкой
    print(line)

myFile = open('filename.txt', 'W', encoding="utf8") #ставим W чтоб менять файлы
myFile.write('ttt') #можно так добавить в файл строку

print('tt', file=myFile) #можно так

with open("filename.txt") as myFile: #чтоб закрыть файл для безопасности от открытых файлов
    for line in myFile:
        print(line)

#Эта программа сдвигает буквы написанные нами то есть если сдвиг 2 то вместо "а" выдаст "в"
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''
def changeChar(char):
    if char in alpha: #если буква есть в первом алфавите то работаем с ним
        return alpha[(alpha.index(char) + number) % len(alpha)] #len чтоб если цифра была больше 32 то отсчет начался заново
    elif char in alphaUp: #если во втором то сним
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char #если ни в том ни в том то просто ввернется заданное значение


with open("filename2.txt", encoding="utf8") as myFile: #у нас есть какой-то текст в этом файле
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", 'w', encoding="utf8") as myFile: #текст из прошлого файла перенесется в новый но уже со сдвигом
    myFile.write(summary)