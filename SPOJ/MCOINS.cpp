#include <stdio.h>
#include <algorithm>

using namespace std;

int win[1000001];

int main(){
    int K,L,m;
    scanf("%d %d %d",&K,&L,&m);
    
    int maxN = 0,N[m];
    
    for(int i = 0;i < m;++i){
        scanf("%d",&N[i]);
        maxN = max(maxN,N[i]);
    }
    
    win[0] = 0;
    
    for(int i = 1;i <= maxN;++i){
       	if(win[i-1] == 0){
       		win[i] = 1;
       	}
       	else{
       		win[i] = 0;
       	}
        if(i >= K && win[i-K] == 0) win[i] = 1;
        if(i >= L && win[i-L] == 0) win[i] = 1;
    }
    
    for(int i = 0;i < m;++i){
        if(win[N[i]]) printf("%s","A");
        else printf("%s","B");
    }
    
    return 0;
}

//DONE