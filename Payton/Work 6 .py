# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
# счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no

print("enter ticket number")

num_ticket = int(input())
first_part = int(0)
second_part = int(0)

if num_ticket > 999999 or num_ticket < 100000:
    print("invalid number")

else:
    first_part = num_ticket // 1000
    second_part = num_ticket % 1000
    if first_part == second_part:
        print("yes")
    else:
        lastnum1 = int(0)
        sum1 = int(0)
        lastnum2 = int(0)
        sum2 = int(0)

        while first_part > 0:
            lastnum1 = first_part%10
            sum1 += lastnum1
            first_part = first_part//10

        while second_part > 0:
            lastnum2 = second_part % 10
            sum2 = sum2 + lastnum2
            second_part = second_part // 10

        if sum1 == sum2:
            print("yes")
        else:
            print("no")