#Напишите программу, которая спрашивает у пользователя
#числа по одному до тех пор, пока он не введёт пустую
#строку. После этого программа должна вывести арифметическое
#среднее всех введённых чисел, а также минимальное
#и максимальное из них.
a = 1
print('Вводите числа')
k = 0
d = 0

while a > 0:
    n = input()
    if n == ' ':
        print('Вы ввели пробел. Введите число')
    else:
        if bool(n) == False:
            break
        else:
            if n.isalpha() == True:
                print('Вы ввели не число. Введите число')
            else:
                n = int(n)
                k = k + n
                d = d + 1
                if d == 1:
                    nmin = n
                    nmax = n
                if n < nmin:
                    nmin = n
                if n > nmax:
                    nmax = n

if d == 0:
    print('Ничего не вышло :( Попробуйте перезапустить программу')
else:
    d = k/d
    d = round(d,3)
    print('Наибольшее =',nmax)
    print('Наименьшее =',nmin)
    print('Среднее арифметическое =',d)
