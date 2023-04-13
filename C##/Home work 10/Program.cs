//Задайте массив вещественных чисел. 
//Найдите разницу между максимальным и минимальным элементов массива.
Console.Clear();
double[] GetArray(int size, double minSum, double maxSum)
{
    double[] result = new double[size];
    for (int i = 0; i < size; i++)
    {
        result[i] = Math.Round(new Random().NextDouble() * (maxSum - minSum) + minSum, 2);
    }
    return result;
}
double ResultMax(double[] inArray)
{
    double max = 0;
    for (int i = 0; i < inArray.Length; i++)
    {
        if (inArray[i] > max)

            max = inArray[i];
    }
    return max;
}
double ResultMin(double[] inArray)
{
    double min = 0;
    for (int i = 0; i < inArray.Length; i++)
    {
        if (inArray[i] < min)

            min = inArray[i];
    }
    return min;
}
double[] array = GetArray(10, -10, 10);

Console.WriteLine(String.Join(", ", array));

double min = ResultMin(array);
double max = ResultMax(array);

Console.WriteLine($"Максимальное = {max}, Минимальное = {min}");
Console.WriteLine($"Разниwа между минимальным и максимальным = {Math.Round(max-min, 2)}");
