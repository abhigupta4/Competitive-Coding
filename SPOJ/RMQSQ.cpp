#include <iostream>
#include <math.h>
#include <limits.h>
using namespace std;

int min(int a, int b){
	if (a < b){
		return a;
	}
	else{
		return b;
	}
}
int range_min_query(int seg_tree[],int qlow, int qhigh, int low, int high, int pos){
	if(qlow <= low && qhigh >= high){
		return seg_tree[pos];
	}
	if(qlow > high || qhigh < low){
		return INT_MAX;
	}
	int mid = (low + high) / 2;
	int left_value = range_min_query(seg_tree,qlow,qhigh,low,mid,(2 * pos) + 1);
	int right_value = range_min_query(seg_tree,qlow,qhigh,mid + 1,high,(2 * pos) + 2);
	return min(left_value , right_value );
}

void construct_tree(int input[],int seg_tree[],int low, int high,int pos){
	if (low == high){
		seg_tree[pos] = input[low];
		return ;
	}
	int mid = (low + high) / 2;

	construct_tree(input, seg_tree, low, mid ,(2 * pos) + 1);

	construct_tree(input, seg_tree, mid + 1, high ,(2 * pos) + 2);
	
	seg_tree[pos] = min(seg_tree[(2 * pos) + 1],seg_tree[(2 * pos) + 2]);

}

int main(){
	int N,Q,qlow,qhigh;
	cin >> N;
	int input[N];
	for(int i = 0; i < N; i++){
		cin >> input[i];
	}
	int x = (int)(ceil(log2(N)));
	int max_size = 2 * (int)pow(2, x) - 1;
	int seg_tree[max_size];
	construct_tree(input,seg_tree,0,N - 1 ,0);
	cin >> Q ;
	while( Q > 0){
		cin >> qlow;
		cin >> qhigh;
		cout << range_min_query(seg_tree,qlow,qhigh, 0, N - 1 , 0) << endl;
		Q--;
	}
	return 0;
}

//DONE