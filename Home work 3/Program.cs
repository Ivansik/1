//Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,является ли этот день выходным.

Console.Clear();
Console.WriteLine("Введите цифру");

int sum = int.Parse(Console.ReadLine()!);
string[] days = new string[] { "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" };

if (sum > 7) Console.WriteLine("Неправильно введен номер дня недели");
else
{
    for (int i = 0; i <= days.Length; i++)
    {
        
        if (days[sum - 1] == "Суббота" ^ days[sum - 1] == "Воскресенье") Console.WriteLine($"День {sum} - выходной {days[sum - 1]}");
        
        else Console.WriteLine($"День {sum} - не выходной {days[sum - 1]}");
        
        break;
    }
}
