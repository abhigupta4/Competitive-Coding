#include <bits/stdc++.h>
#define F first
#define S second

using namespace std;

char input[31000];
pair<int,int> st[4*31000];

void cons(int low, int high,int pos){
	if (low == high){
		if (input[low] == '('){
			st[pos].F = 0;
			st[pos].S = 1;
		}
        else{
            st[pos].F = 1;
            st[pos].S = 0;
        }
		return ;
	}
	int mid = (low+high)/2;
	int l = 2*pos + 1;
	int r = 2*pos + 2;
	cons(low, mid ,l);
	cons(mid+1, high ,r);
	st[pos].F = max(st[r].F - st[l].S,0) + st[l].F;
	st[pos].S = max(st[l].S-st[r].F,0) + st[r].S;
}

void update(int pos,int low,int high,int idx){
    if (low == high){
		st[pos].F = !st[pos].F;
		st[pos].S = !st[pos].S;
		return ;
    }
    int mid = (low+high)/2;
    int l = 2*pos + 1;
    int r = 2*pos + 2;
    if(idx >= low && idx <= mid){
        update(l,low,mid,idx);
    }
    else{
        update(r,mid+1,high,idx);
    }
    st[pos].F = max(st[r].F - st[l].S,0) + st[l].F;
	st[pos].S = max(st[l].S-st[r].F,0) + st[r].S;
}

int main(){
	int test = 1;
	int size,query,k;
	for(int t=1;t<=10;t++){
		scanf("%d",&size);
		scanf("%s",&input);
		cons(0,size-1,0);
		scanf("%d",&query);
		printf("Test %d:\n",&t);
		for(int q=0;q<query;q++){
			scanf("%d",&k);
			if(k!= 0){
				update(0,0,size-1,k-1);
			}
			else{
				if(st[0].F == 0 and st[0].S == 0){
					printf("%s\n","YES");
				} 
				else{
					printf("NO\n");
				}
			}
		}
	}
	return 0;
}