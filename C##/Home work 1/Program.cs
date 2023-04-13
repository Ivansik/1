//*Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.

Console.Clear();

Console.WriteLine("Введите трехзначное число");

int sum = int.Parse(Console.ReadLine()!);
int y = (sum / 10) % 10;

if (sum >= 100 && sum < 1000) Console.WriteLine($"Средняя цифра введенного числа {y}");
else if (sum < 100 ^ sum > 1000) Console.WriteLine($"Число {sum} не трехзначное");
