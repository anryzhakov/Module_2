# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Дополнительное практическое задание по модулю:
# "Основные операторы"

import random

firstFieldList = []
passFieldList = []
Item = 3
while Item <= 20:
    firstFieldList.append(Item)
    Item +=1
firstField = random.choice(firstFieldList)

print(firstField)

for i in range(firstField): #firstField)
    for j in range(firstField):
        k = (i + 1) + (j + 1)
        if firstField > 3:
            if (firstField % k) == 0 and (i < j)  :
                passFieldList.append(i +1)
                passFieldList.append(j +1)
        else: continue
print(passFieldList)