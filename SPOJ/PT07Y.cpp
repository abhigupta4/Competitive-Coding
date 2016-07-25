#include <iostream>
#include <vector> 
#include <map>
using namespace std;

map<int, vector<int> > graph;
int marked[10001];

void dfs(int node){
    marked[node]= 1;
    for(vector<int>::iterator it = graph[node].begin(); it != graph[node].end(); ++it) {
    /* std::cout << *it; ... */
        if(marked[*it] != 1){
            dfs(*it);
        }
    }
}
int main() {
	// your code goes here
	int N,M,a,b,flag,temp;
	cin >> N >> M;
    temp = M;
	while(M > 0){
	    cin >> a >> b;
	    graph[a].push_back(b);
	    graph[b].push_back(a);
	    M--;
	}
	if (N != temp + 1){
        cout << "NO" <<endl;
    }
	   //cout << marked[it->first] << '\n';
    else{
        dfs(a);
    	flag = 0;
    	for (map<int,vector<int> >::iterator it=graph.begin(); it!= graph.end(); ++it){
    	    if (marked[it->first] != 1){
    	        flag = 1;
    	        break;
    	    }
    	}
        if (flag == 1){
            cout << "NO" << endl;
        }
        else{
            cout << "YES" << endl;
        }
    }
	return 0;
}

#DONE