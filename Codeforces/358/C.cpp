#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define F first
#define S second
#define sd(a) scanf("%d",&a)
#define sdl(a) scanf("%lld",&a)
#define pd(a) printf("%d\n",a)
#define pdl(a) printf("%lld",a)
#define mp make_pair
#define pb push_back
#define FOR(i, a, n) for(int i = (a); i < (n); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define MOD 1000000007
#define pii pair<int,int>

vector<pii> g[123456];
ll values[123456];
int count1=0;

void dfs(int node,int dist){
	if (values[node] < dist){
		return;
	}
	// pd(1);
	count1 += 1;
	// pd(node);
	REP(i,g[node].size()){
		dfs(g[node][i].F,max(0,dist+g[node][i].S));
	}
	return;
}

int main(){
	int n;
	sd(n);
	REP(i,n){
		sdl(values[i+1]);
	}
	int a,b;
	REP(i,n-1){
		sd(a);sd(b);
		g[a].pb(mp(i+2,b));
	}
	dfs(1,0);
	pd(n-count1);
	return 0;
}