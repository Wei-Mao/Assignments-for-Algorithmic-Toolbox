#include <iostream>
#include <cassert>
// Dividend / divisor = quotient.....remainder
int gcd_naive(int a, int b) {
  // Linear Search for the Greatest Common Divisor of a and b
	// runtime approximates O(max{a,b}) inefficiently
  /* int current_gcd = 1; */
  /* for (int d = 2; d <= a && d <= b; d++) { */
  /*   if (a % d == 0 && b % d == 0) { */
  /*     if (d > current_gcd) { */
  /*       current_gcd = d; */
  /*     } */
  /*   } */
  /* } */

  /* return current_gcd; */
  /*
	Let a' be the remainder when a is divided by a, then 
	gcd(a,b) = gcd(a', b) = gcd(b, a')
  */
  // Recursive Algorithm based on the Key Lemma
  // Euclidean Algorithm
	assert(a>=0 && a<= 2e9);
	assert(b>=0 && a<= 2e9);
	// Swap a and b such that a is greater than or equal to b
	if(a < b)
	{
		int temp(a);
		a = b;
		b = temp;
	}

	// base case
	if(b == 0)
	{
		return a;
	}
	
	// Update a to be the remainder of a/b
	a = a % b;
	return gcd_naive(a, b);
}

int main() {
  int a, b;
  std::cin >> a >> b;  // continuous inputs
  std::cout << gcd_naive(a, b) << std::endl;
  return 0;
}
