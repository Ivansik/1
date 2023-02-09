// Задача 21: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

Console.Clear();

Console.WriteLine("Введите координаты x1:");
int x1 = int.Parse(Console.ReadLine()!);
Console.WriteLine("Введите координаты y1:");
int y1 = int.Parse(Console.ReadLine()!);
Console.WriteLine("Введите координаты z1:");
int z1 = int.Parse(Console.ReadLine()!);

Console.WriteLine("Введите координаты x2:");
int x2 = int.Parse(Console.ReadLine()!);
Console.WriteLine("Введите координаты y2:");
int y2 = int.Parse(Console.Re21adLine()!);
Console.WriteLine("Введите координаты z2:");
int z2 = int.Parse(Console.ReadLine()!);

double res = Math.Round(Math.Sqrt(Math.Pow(x1-x2, 2) + Math.Pow(y1-y2, 2) + Math.Pow(z1-z2, 2)), 2);

Console.WriteLine($"Расстояние между тремя точками в 3D пространстве: {res}");