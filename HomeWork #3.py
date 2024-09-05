# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

# 1.Запишите исходный список в переменную my_list.
my_list = [0, 42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
k = len(my_list)

# 2.Напишите цикл while с соответствующими задаче условиями.
while i < k:

    if my_list[i] > 0:
        print(my_list[i])
        i += 1
    elif my_list[i] == 0:
        i += 1
        continue
    else:
        break