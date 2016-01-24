#include <iostream>
using namespace std;

int cache[2001][2001];
int val[2001];
int N;

int max(int a,int b){
    if (a > b){
        return a;
    }
    return b;
}

int profit(int begin,int end){
    if(begin > end){
        return 0;
    }
    int year = N - (end - begin + 1) + 1;
    if(cache[begin][end] != -1){
        return cache[begin][end];
    }
    return cache[begin][end] = max(profit(begin + 1, end) + year * val[begin],profit(begin,end - 1) + year * val[end]);
    
}

int main() {
	int i,j;
	for(i = 0; i < 2001; i++){
	    for(int j = 0; j < 2001 ; j++){
	        cache[i][j] = -1;
	    }
	}
	cin  >> N;
	for(i = 0; i < N; i++){
	    cin >> val[i];
	}
	cout << profit(0,N - 1);
	return 0;
}

#DONE