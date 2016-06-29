#include <bits/stdc++.h>
using namespace std;

#define pb push_back

vector<int> adj[2100];
int color[2100];

void bipartite(int n){
	for(int i=1;i<=n;i++){
		color[i] = -1;
	}
	queue<int> qu;
	for(int indx=1;indx<=n;indx++){
		if (color[indx] == -1){
			color[indx] = 0;
			qu.push(indx);
			while(!qu.empty()){
				int curr = qu.front();
				qu.pop();
				for(int vert = 0;vert < adj[curr].size();vert++){
					if(color[adj[curr][vert]] == -1){
					    qu.push(adj[curr][vert]);
						color[adj[curr][vert]] = 1 - color[curr];
					}
					else if(color[adj[curr][vert]] == color[curr]){
						printf("%s\n","Suspicious bugs found!");
						return;
					}
				}
			}
		}
	}
	
	printf("%s\n","No suspicious bugs found!");
}

int main(){
	int test,n,inter,u,v;
	scanf("%d",&test);
	for(int t=0;t<test;t++){
		scanf("%d %d",&n,&inter);
		for(int i=1;i<=n;i++){
			adj[i].clear();
		}
		for(int ed = 0;ed < inter;ed++){
			scanf("%d %d",&u,&v);
			adj[u].pb(v);
			adj[v].pb(u);
		}
		printf("Scenario #%d:\n",t+1);
		bipartite(n);
	}
	return 0;
}