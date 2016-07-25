#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define max1 183*183

using namespace std;

int main(){
    int T,n,m,color,row,col,sr,sc,l,r;
    unordered_map<pair<int,int>,int> seen;
    queue<pair<int,int> > q;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        scanf("%d %d",&n,&m);
        int bitmap[n][m];
        int ans[n][m];
        vector<pair<int,int> > source;
        for(row=0;row<n;row++){
            for(col=0;col<m;col++){
                scanf("%d",&color);
                bitmap[row][col] = color;
                ans[row][col] = max1;
                if(color == 1){
                    source.pb(mp(row,col));
                }
            }
        }
        for(int s=0;s < source.size();s++){
            sr = source[s].first;
            sc = source[s].second;
            q.push(source[s]);
            while(!q.empty()){
                pair<int,int> node = q.front();
                // if(q.size() > 10){
                //     break;
                // }
                seen[node] = 1;
                q.pop();
                l = node.first;
                r = node.second;
                cout << l << " " << r << endl;
                ans[l][r] = min(ans[l][r],abs(sr-l)+abs(sc-r));
                if (l > 0 && bitmap[l-1][r] != 1){
                	if (seen.find(mp(l-1,r)) == seen.end()){
	                    q.push(mp(l-1,r));
                 	}
                }
                if(l < n-1 and bitmap[l+1][r] != 1){
                	if(seen.find(mp(l+1,r)) == seen.end()){
	                    q.push(mp(l+1,r));
                	}
                }
                if(r > 0 and bitmap[l][r-1] != 1){
                	if(seen.find(mp(l,r-1)) == seen.end()){
	                    q.push(mp(l,r-1));
                	}
                }
                if(r<m-1 and bitmap[l][r+1] != 1){
                	if(seen.find(mp(l,r+1)) == seen.end()){
	                    q.push(mp(l,r+1));
                	}
                }
            }
            // while(!q.empty()) q.pop();
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                printf("%d ",ans[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}