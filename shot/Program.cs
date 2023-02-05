// Определить колличество цифр в числе

Console.Clear();

Console.Write("Введите число ");
int num = int.Parse(Console.ReadLine()!);


int count = 0;
while (num /10 != 0)
{
    num = num /10;
    count++;
}

Console.WriteLine(count+1);
