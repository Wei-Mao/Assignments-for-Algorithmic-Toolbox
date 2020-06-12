#include <iostream>

/*
	Euclidean Algorithm to figure out the gcd
*/
int gcd_fast(int a, int b)
{
	// Ensure that a is not less than b
	if(a < b)
	{
		int temp(a);
		a = b;
		b = temp;
	}
	
	if(b == 0)
	{
		return a;
	}
	
	// change value of a to be the remainder of  a/b
	a = a % b;
	return gcd_fast(a, b);
}

long long lcm_naive(int a, int b) {
	// Linear Search
  /* for (long l = 1; l <= (long long) a * b; ++l) */
  /*   if (l % a == 0 && l % b == 0) */
  /*     return l; */

  /* return (long long) a * b; */

  /*
	For two numbers ‘a’ and ‘b’, LCM x GCD = a x b
  */
  // Step1:Find the Greatest Common Divisor of a and b
	int gcd = gcd_fast(a,b);
	
  // Step2: product
	long long prd = (long long) a * b;

	return (long long) prd / gcd;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm_naive(a, b) << std::endl;
  return 0;
}
