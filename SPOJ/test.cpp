#include <iostream>
#include <cstring>
#include <cstdio>
#define MAX 46656
#define LMT 216
#define LEN 4830
#define RNG 100032
#define sq(x) ((x)*(x))
#define mset(x,v) memset(x, v , sizeof(x))
#define chkC(x,n) (x[n >> 6] & (1 << ((n >> 1) & 31)))
#define setC(x,n) (x[n >> 6] |= (1 << ((n >> 1) & 31)))
using namespace std;
unsigned base[MAX/64], segment[RNG/64], primes[LEN];

/* 
 * Generates all the necessary prime numbers and marks them in base[]
 */

int main() {
    for(int z = 0; z < 729; z++) {
        printf("base[%d]: %u\n", z, base[z]);
    }
    setC(base, 9);
    printf("base[0]: %u", base[0]);
    // unsigned i, j, k;
    // for (i = 3; i < LMT; i += 2) {
    //     if (!chkC(base, i)) {    
    //         for (j = i * i, k = i << 1; j < MAX; j += k)
    //             setC(base, j);
    //     }
    // }
    // for(int z = 0; z < 729; z++) {
    //     printf("base[%d]: %u\n", z, base[z]);
    // }
    return 0;
}