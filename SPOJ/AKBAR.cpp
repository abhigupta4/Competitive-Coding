#include <bits/stdc++.h>
#define pb push_back

using namespace std;

unordered_map<long int,int> visited;
vector<long int> seen;
unordered_map<long int,int> local;
vector<long int> adj[100001];

int bfs(long int start,long int power){
	long int temp = power;
	long int cur;
	vector<long int> qu;
	qu.pb(start);
	while(!qu.empty()){
		cur = qu[0]; 
		qu.erase(qu.begin());
		if (local.find(cur) == local.end() and visited.find(cur) != visited.end()){
			return -1;
		}
		if(local.find(cur) == local.end()){
			seen.pb(cur);
			local[cur] = visited[cur] = 1;
		}
		else{
			continue;
		}
		if(temp > 0){
			for(long int var = 0;var < adj[cur].size();var++){
				if (local.find(adj[cur][var]) == local.end()){
					qu.pb(adj[cur][var]);
				}
			}
		}
		temp--;
	} 
	return 0;
}

int main(){
	int T,check,flag;
	long int N_cities,R_edges,M_sol,e,f,sol,pow1;
	scanf("%d",&T);
	for(int t = 0;t<T;t++){
	    visited.clear();
	    seen.clear();
	    local.clear();
	    flag = 0;
	    for(long int f = 0;f < 100001;f++){
	        adj[f].clear();
	    }
		scanf("%ld %ld %ld",&N_cities,&R_edges,&M_sol);
		long int sold[M_sol][2];
		for(long int r = 0;r < R_edges;r++){
			scanf("%ld %ld",&e,&f);
			adj[e].pb(f);
			adj[f].pb(e);
		}
		for(long int s = 0;s<M_sol;s++){
			scanf("%ld %ld",&sol,&pow1);
			sold[s][0] = sol;
			sold[s][1] = pow1;
		}
		for(long int s = 0;s<M_sol;s++){
            check = bfs(sold[s][0],sold[s][1]);
            local.clear();
            if(check == -1){
                flag = 1;
                break;
            }
		}
		if(seen.size() == N_cities and flag != 1){
		    cout << "Yes"<< endl;
		}
		else{
		    cout << "No" << endl;
		}
	}
	return 0;
}