#include <bits/stdc++.h>
using namespace std;

int main(){
	int n,t;
	int i,p;
	char g[200002];
	scanf("%d%d%s",&n,&t,g+1);
	g[0] = '0';
	for(p=1;p<=n && g[p] != '.';p++);
	for(i=p+1;i<=n && g[i] < '5';i++);
	if(i>n){
		printf("%s\n",g+1);
		return 0;
	}
	for(i--;p<i && t>0;i--){
		if (g[i+1] >= '5'){
			g[i]++;
			g[i+1] = '\0';
			t--;
		}
	}
	if (g[p+1] >= '5' && t){
		g[p--] = '\0';
		while(g[p] == '9'){
			g[p--] = '0';
		}
		g[p]++;
		if(p==0){
			printf("%s\n",g);
			return 0;
		}
	}
	printf("%s\n",g+1);
	return 0;

}