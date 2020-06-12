#include <iostream>
#include <vector>
#include <cassert>
using std::vector;

long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    long long sum = 0;

    long long current = 0;
    long long next  = 1;

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current;
        }

        long long new_current = next;
        next = next + current;
        current = new_current;
    }

    return sum % 10;
}

// Figure out the last digit of the sum of Fibonacci Numbers
/*
   Fast algorithm requires coming up with an unique insight into the task
   Based on the Formula of Sum of Fibonacci Numbers, the formula for partial sum of the mth elements to nth elements is given by
   F_{n+2} - F_{m+1}
*/

long long get_fibonacci_huge_fast(long long n, long long m) {
  // find the last digit of Fn mod m efficiently
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

int get_fibonacci_partial_sum_fast(long long from, long long to)
{
    assert(from <= to && from >=0 && to <=1e14);
    int a = get_fibonacci_huge_fast(to + 2, 10);   
    int b = get_fibonacci_huge_fast(from +1, 10);
    
    if(a >=b)
    {
      return a - b;
    }
    else
    {
      return 10 + a - b;
    }
    
}
int main() {
    long long from, to;
    std::cin >> from >> to;
    /* std::cout << get_fibonacci_partial_sum_naive(from, to) << '\n'; */
    std::cout << get_fibonacci_partial_sum_fast(from, to) << '\n';
}
