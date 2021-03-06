#Вариант-5

#Мастям игральных карт присвоены порядковые номера: 1– пики, 2 – трефы, 3 – бубны, 4 –
#червы. Достоинству карт, старших десятки, присвоены номера: 11 – валет, 12 – дама, 13 –
#король, 14 – туз. Дано трехзначное число, в котором первая цифра указывает на масть, а
#вторые две на достоинство карты. Вывести соответствующее название карты вида «дама
#червей», «туз треф» и т.п.

tbl1 = {
    1: 'пики',
    2: 'трефы',
    3: 'бубны',
    4: 'червы'
}

tbl2 = {
    11: 'валет',
    12: 'дамы',
    13: 'король',
    14: 'туз'
}

minVal, maxVal = 111, 414

# Функция исполняет определение числа
# из трехзначного числа.
# Идет градация 0 = 1-ое число с конца
# Идет градация 1 = 2-ое число и т.д.
def getDigit(number, n):
    return number // 10 ** n % 10

num = input('Введите трехзначное число. Число не должно быть меньше {} и больше {}: '.format(minVal, maxVal))
while type(num) != int:
    try:
        num = int(num)

        if num > maxVal:
            print('Введено слишком большое число - {}. Число не должно быть больше {}'.format(num, maxVal))
            num = input('Введите трехзначное число. Число не должно быть меньше {} и больше {}: '.format(minVal, maxVal))
        elif minVal > num:
            print('Введено слишком маленькое число - {}. Число должно быть больше {}'.format(num, minVal))
            num = input('Введите трехзначное число. Число не должно быть меньше {} и больше {}: '.format(minVal, maxVal))
    except ValueError:
        print('Введено не целое число!')
        num = input('Введите трехзначное число: ')

#Переводим последние две цифры в строку, для получения двузначного числа и снова переводим в число
#для вывода по ключу таблицы значения
secVal = int(str(getDigit(num, 1)) + str(getDigit(num, 0)))

#Проверка на наличие ключа в таблице
if secVal not in tbl2:
    print("Ключа {} не существует в таблице".format(secVal))
else:
    print(tbl2[secVal], tbl1[getDigit(num, 2)])
