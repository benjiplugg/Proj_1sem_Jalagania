# Вариант - 5

# Дан словарь с произвольным количеством элементов.
# Выяснить имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует,
# о добавить его в словарь. Вывести на экран первоначальный словарь и измененный.

dictionary = dict()

dictionary['овощи'] = 'огурец'
dictionary['мясо'] = 'хамон'
dictionary['напиток'] = 'лимонад'

# Цикл на поиск ключа 'фрукт'
for key in dictionary:
    if key != 'фрукт' and dictionary[key] != 'яблоко':
        print(dictionary)

        dictionary.update({'фрукт':'яблоко'})

        print(dictionary)

        break
