#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
#define sd(x) scanf("%d",&x)
#define psi pair<string,int>
#define pii pair<int,int>
 
using namespace std;
 
vector<vector<pair<int, int> > > g;
vector<ll> sdist;
map<string,int> name1;
 
void dij(int start,int end){
	priority_queue<pii,vector<pii >,greater<pii > > qu;
	qu.push(mp(0,start));
	unordered_map<int,int> seen;
	while(!qu.empty()){
		pii v1cost;
		v1cost = qu.top();
		qu.pop();
		int v1 = v1cost.S;
		int cost = v1cost.F;
		if(seen.find(v1) == seen.end()) {
			seen[v1] = 1;
			sdist[v1] = cost;
			if (v1==end){
		        return ;
		    }
			for(int i = 0; i < g[v1].size(); i++) {
				int c = g[v1][i].F;
				int v2 = g[v1][i].S;
				if(seen.find(v2) == seen.end()) {
					qu.push(mp(cost+c, v2));
				}
			}
		}
	}
}
 
int main(){
	int test,n,city,con,next,dist,query;
	char name[20];
	char space;
	sd(test);
	for(int t=0;t<test;t++){
		name1.clear();
		g.clear();
		sdist.clear();
		sd(city);
		for(int c=0;c<city;c++){
			vector<pair<int,int> > emp;
			g.pb(emp);
			scanf("%s",name);
			name1.insert(psi(name,c));
			sd(con);
			for(int co=0;co<con;co++){
				sd(next);
				sd(dist);
				g[c].pb(mp(dist,next-1));
			}
		}
		sd(query);
		for(int q=0;q<query;q++){
			for(int j=0;j<city;j++){
				sdist.pb(-1);
			}
			char t1[20];
			char t2[20];
			scanf("%s %s",t1,t2);
			dij(name1[t1],name1[t2]);
			printf("%d\n",sdist[name1[t2]]);
		}
		scanf("%c",&space);
	}
	return 0;
}