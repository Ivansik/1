# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

N = int(input("enter number: "))
list = []
count0 = 0
count1 = 0
for _ in range(N):
    list.append(random.randint(0,1))
print(list)
for i in list:
    if i == 0:
        count0 += 1
    else:
        count1 += 1
if count0 < count1:
    print(count0)
else:
    print(count1)