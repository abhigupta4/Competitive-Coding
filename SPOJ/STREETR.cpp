#include <iostream>

using namespace std;

int gcd(int a,int b){
	if (b == 0){
		return a;
	}
	else{
		return gcd(b, a % b);
	}

}

int main(){
	int N,i;
	cin >> N;
	int coordi[N],diff[N],gcd_fin;
	for(i = 0; i < N; i++){
		cin >> coordi[i];
	}
	gcd_fin = coordi[1] - coordi[0];
	for(i = 1;i < N - 1; i++){
		gcd_fin = gcd(gcd_fin,coordi[i + 1] - coordi[i]);
	}
	cout << ((coordi[N - 1] - coordi[0])/ gcd_fin) - N + 1;
	return 0;
}

#DONE