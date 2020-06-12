#include <iostream>

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

	// We only focus on the addition of the last digit
	// Hence, the following logic updates the last digit only
    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
		// update previous
        previous = current;
		// update current
        current = (tmp_previous + current) % 10; // take the remainder
    }

    return current;
}

int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_naive(n);
    std::cout << c << '\n';
    }
