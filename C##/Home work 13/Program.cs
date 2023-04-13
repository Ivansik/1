//Пользователь вводит с клавиатуры M чисел. Посчитайте,сколько чисел больше 0 ввёл пользователь.

Console.Clear();

Console.WriteLine("Введите последовательно числа");
Console.WriteLine("Какое количество цифр вы хотите ввести?");

int m = int.Parse(Console.ReadLine()!);


int[] GetArray(int m)
{
    int[] array = new int[m];
    for (int i = 0; i < m; i++)
    {
        Console.WriteLine($"Введите число № {i + 1}");
        array[i] = int.Parse(Console.ReadLine()!);
    }
    return array;
}

int AfterZero(int[] array)
{
    int result = 0;
    foreach (var item in array)
    {
        if(item > 0)
        {
            result += 1;
        }
    }
    return result;
}

int[] newArray = GetArray(m);
Console.WriteLine(String.Join(", ", newArray));

int afterZero = AfterZero(newArray);
Console.WriteLine($"Из введённого количества {afterZero} цифр - больше 0!");

