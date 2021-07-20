using System;
using System.Collections.Generic;
using System.Linq;

namespace QuickSortCS
{
    class Program
    {
        static void Main(string[] args)
        {
            var result = QuickSort(new List<int> { 10, 5, 2, 3 });
            Display(result);
        }

        static List<int> QuickSort(List<int> array)
        {
            // Warunek podstawowy, jeżeli są mniej niż dwa elementy w tabeli to znaczy że nie trzeba jej sortować
            if (array.Count < 2)
            {
                return array;
            }

            int pivot = array[0];
            var lesser = array.Skip(1).Where((i) => i <= pivot).ToList();
            var greater = array.Skip(1).Where((i) => i > pivot).ToList();


            var result = new List<int>();
            result.AddRange(QuickSort(lesser));
            result.Add(pivot);
            result.AddRange(QuickSort(greater));
            return result;
        }

        static void Display(List<int> array)
        {
            System.Console.WriteLine($"[{String.Join(", ", array)}]");
        }
    }
}
