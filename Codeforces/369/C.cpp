#include <bits/stdc++.h>
using namespace std;
#define inf 1345678912345
#define ll long long


ll dp[104][104][104];

int main(){
	int n,m,kk;
	int col[110];
	int cost[110][110];
	cin >> n >> m >> kk;
	for(int i=0;i<n;i++){
		cin >> col[i];
		col[i]--;
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin >> cost[i][j];
		}
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<=n;j++){
			for(int k=0;k<m;k++){
				dp[i][j][k] = inf;
			}
		}
	}
	if (col[0] == -1){
		for(int i=0;i<m;i++){
			dp[0][1][i] = cost[0][i];
		}
	}
	else{
		dp[0][1][col[0]] = 0;
	}
	for(int i=1;i<n;i++){
		for(int j=1;j<=n;j++){
			if (col[i] == -1){
				for(int k=0;k<m;k++){
					for(int l=0;l<m;l++){
						if(l!=k){
							dp[i][j][k] = min(dp[i-1][j-1][l] + cost[i][k],dp[i][j][k]);
						}
						else{
							dp[i][j][k] = min(dp[i-1][j][l]+cost[i][k],dp[i][j][k]);
						}
					}
				}
			}
			else{
				for(int l=0;l<m;l++){
					if (l != col[i]){
						dp[i][j][col[i]] = min(dp[i-1][j-1][l],dp[i][j][col[i]]);
					}
					else{
						dp[i][j][col[i]] = min(dp[i-1][j][l],dp[i][j][col[i]]);
					}
				}
			}
		}
	}
	ll ans = inf;
	for(int i=0;i<m;i++){
		ans = min(ans,dp[n-1][kk][i]);
	}
	if(ans == inf){
		cout << -1 << endl;
	}
	else{
		cout << ans << endl;
	}
	
	return 0;
}