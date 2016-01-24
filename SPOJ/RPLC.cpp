#include <iostream>

using namespace std;

int main(){
	int T,N,neg_sum,sum,temp;
	cin >> T;
	for(int i = 0;i < T;i++){
		cin >> N;
		neg_sum = 0;
		sum = 1;
		for(int j = 0;j < N;j++){
			cin >> temp;
			sum += temp;
			if (sum <= 0){
				neg_sum += (-1 * sum) + 1;
				sum = 1;
			}
		}
		cout << "Scenario #" << i + 1 << ": " << (neg_sum) + 1 << endl;
	}
	return 0;
}

#DONE