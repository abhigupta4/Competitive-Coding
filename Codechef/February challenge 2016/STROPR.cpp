#include <iostream>
#include <stdio.h>
#define MOD 1000000007

using namespace std;

long long int gcdExtended(long long int a,long long int b,long long int *x,long long int *y);

long long int modInverse(long long int a,long long int m)
{
    long long int x, y;
    long long int g = gcdExtended(a, m, &x, &y);
    if (g != 1)
        cout << "Inverse doesn't exist";
    else
    {
        // m is added to handle negative x
        long long int res = (x%m + m) % m;
        return res;
    }
}
 
// C function for extended Euclidean Algorithm
long long int gcdExtended(long long int a,long long int b,long long int *x,long long int *y)
{
    // Base Case
    if (a == 0)
    {
        *x = 0, *y = 1;
        return b;
    }
 
    long long int x1, y1; // To store results of recursive call
    long long int gcd = gcdExtended(b%a, a, &x1, &y1);
 
    // Update x and y using results of recursive
    // call
    *x = y1 - (b/a) * x1;
    *y = x1;
 
    return gcd;
}

int main(){
    int T;
    long int x,N;
    long long int M,val,coeff,temp;
    scanf("%d",&T);
    //cout << "Hi";
    for(int i = 0;i < T;i++){
        scanf("%ld %ld %lld", &N, &x, &M);
        long long int arr1[N];
        for(long int j = 0;j< N;j++){
            scanf("%lld",&arr1[j]);
        }
    //     cout << "Hey";
        if(x == 1){
            val = arr1[0] % MOD;
            //M = 0;
        }
        else if(x == 2){
            val = (((M% MOD) * (arr1[0]% MOD))% MOD + arr1[1]% MOD)% MOD;
            //M = 0;
        }
        else{
            val = arr1[x - 1];
            x -= 2;
            coeff = M;
            temp = 1;
            while(x >= 0)
            {
                //cout << "Val is" << val<< endl;
                val += ((arr1[x] % MOD) * (coeff % MOD))% MOD;
                //cout << "Val is" << val<< endl;
                coeff = ((coeff%MOD * ((M%MOD + temp%MOD)%MOD))%MOD * modInverse(temp + 1,MOD))%MOD;
                //cout << "coeff is" << coeff << endl;
                temp++;
                x--;
            }
        }

    printf("%lld\n",val % MOD);
    }
    return 0;
}   

//DONE