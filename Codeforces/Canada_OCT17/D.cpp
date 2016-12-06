#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define F first
#define S second
#define sd(a) scanf("%d",&a)
#define sdl(a) scanf("%lld",&a)
#define pd(a) printf("%d",a)
#define pdl(a) printf("%lld",a)
#define mp make_pair
#define pb push_back

priority_queue<ll> q1;
priority_queue< pair<ll,ll> > q2;

int main(){
	ll mine,n,wt,bal;
	sdl(n);
	sdl(mine);sdl(wt);
	for(int i=0;i<n-1;i++)
	{
		sdl(bal);sdl(wt);
		if (bal > mine)
		{
			q1.push(bal-wt-1);
		}
		else
		{
			q2.push(mp(bal,wt));
		}
	}
	ll ans = (ll)q1.size();
	while(!q1.empty() and mine >= -q1.top())
	{
		mine -= -q1.top();
		q1.pop();
		while(!q2.empty() and q2.top().F > mine)
		{
			q1.push(q2.top().F-q2.top().S-1);
			q2.pop();
		}
		ans = min(ans,(ll)q1.size());
	}
	ans = min(ans,(ll)q1.size());
	pdl(ans+1);
	return 0;
}