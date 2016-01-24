#include <iostream>
#include <map>
using namespace std;

int main() {
	// your code goes here
	map<int, int> count;	
	int T,N,i,j,start,end,pos,k,max;
	cin >> T;
	for(i = 0;i < T ; i++){
	    cin >> N;
	    max = 0;
	    for(j = 0; j < N; j++){
	       cin >> start >> end;
	       for(k = start;k < end;k++){
	           count[k]++;
	           if (count[k] > max){
	               max = count[k];
	           }
	       }
	    }
	    cout << max << endl;
	    count.clear();
	}

	return 0;
}

//DONE