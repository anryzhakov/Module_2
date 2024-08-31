# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашняя работа по уроку "Условная конструкция.
# Операторы if, elif, else."

first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and second == third and first == third:
    print(3)
elif first != second and second != third and first!= third:
    print(0)
else:
    print(2)