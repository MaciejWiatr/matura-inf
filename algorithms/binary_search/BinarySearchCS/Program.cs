using System;

namespace BinarySearchCS
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] list = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            Console.WriteLine($"Table is {string.Join(", ", list)}");
            Console.WriteLine("What number are you looking for: ");
            var search = int.Parse(Console.ReadLine());
            var result = BinarySearch(list, search);
            Console.WriteLine($"Binary search result is {result}");
            Console.WriteLine($"Number under index of {result} is {list[result]}");
        }

        static int BinarySearch(int[] list, int item)
        {
            int first = 0;
            int last = list.Length - 1;
            while (first <= last)
            {
                var middle = (first + last) / 2;
                int guess = list[middle];
                if (guess == item)
                {
                    return middle;
                }
                if (guess > item)
                { // item ∈ (first;guess)
                    last = guess - 1;
                }
                else if (guess < item)
                { // item ∈ (guess;last)
                    first = guess + 1;
                }
            }
            return -1;
        }
    }
}
