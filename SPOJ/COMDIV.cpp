#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b%a, a);
}

int factors(int numb){
	int count = 0;
	for(int i = 1;i < (int)sqrt(numb) + 1;i++){
		if ((numb%i) == 0){
			if (i*i == numb){
				count += 1;
			}
			else{
				count += 2;
			}
		}
	}
	return count;
}

int main(){
	int test,a,b;
	for(int t=0;t<test;t++){
		scanf("%d %d",&a,&b);
		printf("%d",factors(gcd(a,b)));
	}
	return 0;
}