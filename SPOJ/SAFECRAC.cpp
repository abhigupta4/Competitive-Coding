#include <bits/stdc++>
#define ll long long
#define push_back pb 
#define mod 1000000007
using namespace std;

int main(){
	ll ans[100001][10];
	ans[0] = {1,1,1,1,1,1,1,1,1,1};
	// vector<vector<int> > graph;
	vector<int> graph[10];
	graph[0].pb(7); 
	graph[1].pb(2);
	graph[1].pb(4);
	graph[2].pb(1);
	graph[2].pb(3);
	graph[2].pb(5);
	graph[3].pb(2);
	graph[3].pb(6);
	graph[4].pb(1);
	graph[4].pb(5);
	graph[4].pb(7);
	graph[5].pb(2);
	graph[5].pb(4);
	graph[5].pb(6);
	graph[5].pb(8);
	graph[6].pb(3);
	graph[6].pb(5);
	graph[6].pb(9);
	graph[7].pb(4);
	graph[7].pb(8);
	graph[7].pb(0);
	graph[8].pb(5);
	graph[8].pb(7);
	graph[8].pb(9);
	graph[9].pb(6);
	graph[9].pb(8);

	return 0;
}
//AC