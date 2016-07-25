//AC
#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define max1 183*183

using namespace std;

int main(){
    int T,n,m,row,col,so_r,so_c,temp;
    char color;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        scanf("%d %d",&n,&m);
        char bitmap[n][m];
        int ans[n][m];
        int visited[n][m];
        queue<pair<int,int> > q;
        for(row=0;row<n;row++){
            for(col=0;col<m;col++){
                scanf(" %c",&color);
                bitmap[row][col] = color;
                ans[row][col] = max1;
                visited[row][col] = 0;
                if(color == '1'){
                    q.push(mp(row,col));
                    ans[row][col] = 0;
                    visited[row][col] = 1;
                }
            }
        }
        while(!q.empty()){
            pair<int,int> node = q.front();
            q.pop();
            row = node.first;
            col = node.second;
            temp = ans[row][col];
            if (row > 0 and visited[row-1][col] != 1){
                q.push(mp(row-1,col));
                ans[row-1][col] = temp+1;
                visited[row-1][col] = 1;
            }
            if(row < n-1 and visited[row+1][col] != 1){
                q.push(mp(row+1,col));
                ans[row+1][col] = temp+1;
                visited[row+1][col] = 1;
            }
            if(col > 0 and visited[row][col-1] != 1){
                q.push(mp(row,col-1));
                ans[row][col-1] = temp+1;
                visited[row][col-1] = 1;
            }
            if(col<m-1 and visited[row][col+1] != 1){
                q.push(mp(row,col+1));
                ans[row][col+1] = temp+1;
                visited[row][col+1] = 1;
            }
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