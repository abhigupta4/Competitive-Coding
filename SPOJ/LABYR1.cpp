#include <bits/stdc++.h>
using namespace std;

int max1,n_c,n_r;

void dfs(int s_r,int s_c,int R,int C,int depth,int p_r,int p_c,char arr[][]){
	if(depth > max1){
		n_c = s_c;
		n_r = s_r;
		max1 = depth;
	}
	if(s_r+1 <R and s_r+1 != p_r){
		if(arr[s_r+1][s_c] == '.'){
			dfs(s_r+1,s_c,R,C,depth+1,s_r,s_c,arr[][]);
		}
	}
	if(s_r-1>=0 and s_r-1 != p_r){
		if(arr[s_r-1][s_c] == '.'){
			dfs(s_r-1,s_c,R,C,depth+1,s_r,s_c,arr[][]);
		}	
	}
	if(s_c+1 < C and s_c+1 != p_c){
		if(arr[s_r][s_c+1] == '.'){
			dfs(s_r,s_c+1,R,C,depth+1,s_r,s_c,arr[][]);
		}	
	}
	if(s_c-1 >= 0 and s_c-1 != p_c){
		if(arr[s_r][s_c-1] == '.'){
			dfs(s_r,s_c-1,R,C,depth+1,s_r,s_c,arr[][]);
		}	
	}
}

int main(){
	int test,C,R,s_c,s_r;
	scanf("%d",&test);
	for(int t=0;t<test;t++){
		scanf("%d %d",&C,&R);
		char arr[R][C];
		for(int r=0;r<R;r++){
			for(int c=0;c<C;c++){
				scanf("%c",&char[r][c]);
				if (char[r][c] == '.'){
					s_r = r;
					s_c = c;
				} 
			}
		}
		max1 = 0;
		dfs(s_r,s_c,R,C,0,-1,-1);
		printf("%d %d %d",n_c,n_r,max1);
	}
	return 0;
}