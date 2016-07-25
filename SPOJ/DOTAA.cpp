#include <iostream>
using namespace std;

int main(){
	int T,N,M,M_power;
	int N_power,q;
	cin >> T;
	while (T > 0){
		cin >> N >> M >> M_power;
		while ( N > 0){
			cin >> N_power;
			if (N_power > M_power){
				q = N_power / M_power;
				if ((N_power % M_power) == 0){
					M -= q - 1;
				}
				else{
					M -= q;
				}
			}
			N--;
		}
		if ( M <= 0){
			cout << "YES" << endl;
			cout << endl;
		}
		else{
			cout << "NO" << endl;
			cout << endl;
		}
		T--; 
	}	
	return 0;
}

//DONE