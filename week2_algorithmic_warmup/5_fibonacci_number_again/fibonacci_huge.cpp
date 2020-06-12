#include <iostream>
#include <vector>

long long get_fibonacci_huge_naive(long long n, long long m) {
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

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge_naive(n, m) << '\n';
}
