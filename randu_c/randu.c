#include <stdio.h>

void main() {
    
    return 0; 

}

int randu(x: int) {
    (x * 65539) % 2147483648; 
}

array[int] get_randu_values(seed: int, n: int) {
    int[n] rand_numbers; 

    for (int i = 0; i++; i<n) {
        rand_numbers[i] = randu(seed); 
        seed = rand_numbers[i]; 
    }

    return rand_numbers
}