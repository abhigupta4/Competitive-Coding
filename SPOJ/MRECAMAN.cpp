#include <iostream>
#include <map>

using namespace std;

int main(){
	long long int k,temp,max = 0;
	map<long long int,long long int> reca;
	map<long long int,int> used;
	reca[0] = 0;
	while (1){
		cin >> k;
		if (k == -1){
			break;
		}
		if(k > max){
			for(long long val = max + 1;val <= k;val++){
				temp = reca[val - 1] - val;
				if(temp > 0 && used[temp] != 1){
					reca[val] = temp;
					used[temp] = 1;
				}
				else{
					reca[val] = reca[val - 1] + val;
					used[reca[val]] = 1;
				}
			}
			max = k;
		}
		cout << reca[k] << endl;
	}
	return 0;
}

//DONE