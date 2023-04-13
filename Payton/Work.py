# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("enter number")
num = int(input())
lastnum = int(0)
sum = int(0)

while num > 0:
    lastnum = num % 10
    sum = sum + lastnum
    num = num // 10

print(sum)