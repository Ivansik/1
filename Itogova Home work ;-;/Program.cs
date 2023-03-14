/*Написать программу, которая из имеющегося массива строк формирует массив из строк, длина которых меньше либо равна 3 символа.
Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.*/
Console.Clear();
void SecondArrayWithIF(string[] arr, string[] inArray)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
    if(arr[i].Length <= 3)
        {
        inArray[count] = arr[i];
        count++;
        }
    }
}
void PrintArray(string[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"{array[i]} ");
    }
    Console.WriteLine();
}
string[] arr = new string[10] {"", "При", "Шиш", "Ур", "Игра", "Чат", "Бот", "Сл", "Зи", ""};
string[] inArray = new string[arr.Length];
SecondArrayWithIF(arr, inArray);
PrintArray(inArray);