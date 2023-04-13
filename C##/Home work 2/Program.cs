//*Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.

Console.Clear();
Console.WriteLine("Введите трехзначное число");

int sum = int.Parse(Console.ReadLine()!);
int sum2 = sum % 10;

if (sum >= 100 && sum < 1000) Console.WriteLine($"Третья цифра введенного числа {sum2}");
else if (sum < 100 ^ sum > 1000) Console.WriteLine("Третьей цифры нет");
