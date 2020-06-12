#include "iostream"
#include "vector"
#include "algorithm"
#include "cstdlib"

long long int MaxPairwiseProduct(const std::vector<long long int>& numbers) {
    long long int max_product = 0;
    int n = numbers.size();

    /* for (int first = 0; first < n; ++first) { */
    /*     for (int second = first + 1; second < n; ++second) { */
    /*         max_product = std::max(max_product, */
    /*             numbers[first] * numbers[second]); */
    /*     } */
    /* } */
	// find the first largest number 
	
    int	idx_1st = -1;  // keep track of the 1st lagest number 	
	for(int first = 0; first < n; ++first){
		if(idx_1st == -1 || (numbers[first] > numbers[idx_1st])){
			idx_1st = first;
		}
	}
	// Note that || has the property of short-circuitting, so if idx_1st = -1, numbers[-1] is not parsed! uses short-circuit evaluation
		
	int idx_2nd = -1;
	for(int second = 0; second < n; ++second){
		if((second != idx_1st) && (idx_2nd == -1 || numbers[second] > numbers[idx_2nd])){
			idx_2nd = second;
		}
	}
	/* std::cout << idx_1st << ", " << idx_2nd << std::endl; */
	max_product = (long long int) (numbers[idx_1st] * numbers[idx_2nd]);
    return max_product;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<long long int> numbers(n);
	// read the input sequence of numbers
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
