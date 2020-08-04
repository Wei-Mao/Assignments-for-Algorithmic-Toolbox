#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

template <typename T>  // T should be either integer or floating point type
int binary_search(const vector<T> & A, T k, int low, int high)
{
   /* Searching in a sorted array.
      Input:
	    A(vector<T>): A is the reference sorted array of doubles/integers in ascending order.
	    k(T): The target number which you want to search the array for.
	    low(int): The index pointing to the lower bound of the searched part of the array.
	    high(int): The index pointing to the upper bound of the searched part of the array.
      Output:
	    An index i in the range of low to high where:
	    case 1: A[i] =  k
	    case 2: the greatest index such that A[i] < k
	    case 3: k < A[low], i = low - 1.
      Time Complexity: O(logn)
      Space Complexity: A stack of logn levels. 
      Notes: reference saves a lot of storage space during recursive calls.
      Remarks: Bineary Search is applicable to array due to the constant-time access! List Stack Queue  can not support binary search because they does not support computing the middle point
   */ 
  
  // base case
  if(low > high)
  {
    return low - 1;
  }

  // compute the middle point
  int mid = low + (high - low) / 2; // automatically take the floor thanks to the truncating.

  // divide and conquer
  if(A[mid] == k)
  {
    return mid;
  }
  else if(A[mid] < k)
  {
    return binary_search(A, k, mid + 1, high);   // If low==high, goes to low > high, 
  }
  else
  {
    return binary_search(A, k, low, mid - 1);    // if low==high, goes to low > high.
  }
}




int main()
{
  int n;
  int k;

  cout << "The number of numbers: " << endl;
  cin >> n;
  
  cout << "The sequence of numbers to be searched: " << endl;

  vector<int> a(n);
  for(int i(0); i < n; i++)
  {
    cin >> a[i];
  }

  cout << "The target number: " << endl;
  cin >> k;
  cout<< "The best matched index: " << binary_search<int>(a, k, 0, n-1) << endl;


}
