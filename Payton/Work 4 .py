# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print("enter total")
S = int(input())
Pet = int(0)
Ser = int(0)
Kat = int(0)

Pet = S / 6
Ser = Pet
Kat = (2/3) * S  
print("Pet did {}".format(Pet))
print("Katya did {}".format(Kat))
print("Ser did {}".format(Ser))