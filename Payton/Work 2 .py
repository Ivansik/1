print ("Введите чило: ")
i = int(input())
a = i % 10 
b = i % 100 
b = b // 10
c = i // 100
Summa = a + b + c
print (Summa)