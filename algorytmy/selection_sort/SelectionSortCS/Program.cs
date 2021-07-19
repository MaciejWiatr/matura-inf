using System;
using System.Collections.Generic;

namespace SelectionSortCS
{
    class Program
    {
        static void Main(string[] args)
        {
            var result = SelectionSort(new List<int> { 5, 3, 6, 2, 10 });
            System.Console.WriteLine(String.Join(", ", result));
        }

        static int FindSmallestElementIndex(List<int> arr)
        {
            int smallest = arr[0];
            int smallestIndex = 0;

            for (int i = 0; i < arr.Count; i++)
            {
                if (arr[i] < smallest)
                {
                    smallest = arr[i];
                    smallestIndex = i;
                }
            }

            return smallestIndex;
        }

        static List<int> SelectionSort(List<int> arr)
        {
            var array = new List<int>(arr); // Muszę stworzyć nową instancję listy ponieważ List jest typu referencyjnego
            var sortedArr = new List<int>();
            foreach (var el in arr)
            {
                var smallestIndex = FindSmallestElementIndex(array);
                var item = array[smallestIndex];
                array.Remove(item);
                sortedArr.Add(item);
            }

            return sortedArr;
        }
    }
}
