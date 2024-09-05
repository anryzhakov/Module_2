# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашняя работа по уроку "Цикл for. Элементы списка.
# Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
N = len(numbers)
# 1.Создайте пустые списки primes и not_primes.
primes = []; notPrimes = []
isPrime = bool
# 2.При помощи цикла for переберите список numbers.
for n in range(N):
    if numbers[n] == 1:
        continue
    for k in range(numbers[n]):
        k += 1
        if k == 1 or k == numbers[n]:
            continue
        isPrime = False
        if (numbers[n] % k) == 0:
            isPrime = True
            break
    if isPrime == True:
        notPrimes.append(numbers[n])
    else:
        primes.append(numbers[n])
print('Список простых чисел:   ', primes)
print('Список составных чисел: ', notPrimes)

# P.S.: Простые числа - это натуральные числа, имеющие два
#               различных делителя: единицу и само это число
#       Составные числа - это натуральные числа, которые можно
#               разложить в произведение двух множителей, больших
#               единицы, и имеющие больше двух делителей
