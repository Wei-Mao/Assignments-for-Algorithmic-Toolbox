#include <iostream>
#include <cassert>
#include <vector>

/* int fibonacci_sum_naive(long long n) { */
/*   // Add one addition step to the efficient Fibonacci Sequence */
/*     if (n <= 1) */
/*         return n; */

/*     long long previous = 0; */
/*     long long current  = 1; */
/*     long long sum      = 1; */

/*     for (long long i = 0; i < n - 1; ++i) { */
/*         long long tmp_previous = previous; */
/*         previous = current; */
/*         current = tmp_previous + current; */
/*         sum += current; */
/*     } */

/*     return sum % 10; */
/* } */

// efficient algorithm to compute the Fn
// O(n)
// Figure out the last digit of the sum of Fibonacci Numbers

long long get_fibonacci_huge_fast(long long n, long long m) {
    if (n <= 1)
        return n;


    long long previous = 0;  // 0th Fibonacci Number
    long long current  = 1;  // 1st Fibonacci Number
    std::vector<long long> rem_vec;
    rem_vec.push_back(0);
    rem_vec.push_back(1);
    // n-1 iterations leads to the nth number
    // We only care about the remainder of Fn divided by m
    // i=1: 2th. More generally, i: (i+1)th Number

    long long period(0);

    for (long long i = 1; i < n; ++i) {
	// i is only visible in the for loop
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % m;  // avoid overflow
	/* std::cout << i << ": "<<current << std::endl; */
	rem_vec.push_back(current);
	
	if(previous == 0 && current == 1) // mark the first arrival of the period
	{
	  period = i;
	  break;
	}
    }
    // Do forget the case that the answer is present in the initial period!!!!
    // or write another function to find the period!!!!
    if(period >0)
    {
      long long rem = n % period; 
      return rem_vec[rem];
    }
    else
    {
      return rem_vec[n];
    }
}

/*
   Fast algorithm requires coming up with 
*/
int fibonacci_sum_fast(long long n) 
{
    int last_digit_of_Fn2 = get_fibonacci_huge_fast(n + 2, 10);
    if(last_digit_of_Fn2 == 0)
    { 
      return 9;
    }
    else
    {
      return (last_digit_of_Fn2 - 1) % 10;
    }
}

int main() {
    long long n = 0;
    std::cin >> n;
    /* std::cout << fibonacci_sum_naive(n); */
    std::cout << fibonacci_sum_fast(n);
}
