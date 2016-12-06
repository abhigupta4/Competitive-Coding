#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define pii pair<int,ll>
#define F first
#define S second
#define inf 1345678912
#define sld(a) scanf("%lld",&a)
#define pd(a) printf("%d\n",a)
#define sd(a) scanf("%d",&a)

vector<vector<pii> > g;
ll dp[5002][5002];


ll calc(int cur,int visi){
	if (visi <= 0){
		return inf;
	}
	if(dp[cur][visi] != -1){
		return dp[cur][visi];
	}
	dp[cur][visi] = inf;
	for(int i=0;i<g[cur].size();i++){
		int ele = g[cur][i].F;
		ll ti = g[cur][i].S;
		if (ti+calc(ele,visi-1) <= dp[cur][visi]){
			dp[cur][visi] = ti + calc(ele,visi-1);
		}
	}

	return dp[cur][visi];
}

int main(){
	int n,m,u,v;
	ll time1,ti,ans;
	vector<int> order;
	sd(n);sd(m);sld(time1);
	vector<pii> emp;
	for(int i=0;i<=n;i++){
		for(int j=0;j<=n;j++){
			dp[i][j] = -1;
		}
	}
	dp[1][1] = 0;
	for(int i=0;i<=n;i++){
		g.pb(emp);
	}
	for(int i=0;i<m;i++){
		sd(u);sd(v);sld(ti);
		g[v].pb(mp(u,ti));
	}

	for(int j=n;j >= 2;j--){
		ans = calc(n,j);
		if (ans <= time1){
			pd(j);
			int cur = n;
			order.pb(n);
			int i = j;
			while(cur != 1){
				ll ans = dp[cur][i];
				int t1;
				ll t2;
				for(int k=0;k<g[cur].size();k++){
					t1 = g[cur][k].F;
					t2 = g[cur][k].S;
					if(ans == dp[t1][i-1]+t2){
						order.pb(t1);
						break;
					}
				}
				cur = t1;
				i--;
			}
			order.pb(1);
			for(int i=j-1;i >= 0;i--){
				printf("%d ",order[i]);
			}
			break;
		}
	}
	return 0;
}