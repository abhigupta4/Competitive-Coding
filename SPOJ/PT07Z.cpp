#include<iostream>
#include<map>
#include<vector>

using namespace std;

map<int, vector<int> > graph;

int marked[10001];

int node = -1, maxi = -1;
int count = 1;
    
void dfs(int v) {
	marked[v] = 1;
	for(vector<int>::iterator it = graph[v].begin(); it != graph[v].end(); it++) {
		if(marked[*it] != 1) {
		    count++;
			dfs(*it);
		}
		if(graph[*it].size() == 1){
		    if(count > maxi){
		        //cout << "Hi " << count << " " << *it; 
    		    maxi = count;
    		    node = *it;		        
		    }
		}
	    //count--;
	}
	count--;
}

int main() {
	int N,u, v, i,start_node;
	cin>>N;
	for(int i = 0;i < N -1 ; i++){
	    cin >> u >> v;
	    graph[u].push_back(v);
	    graph[v].push_back(u);
	}
    dfs(u);
	//cout << "Max is " << maxi<<endl;
	//cout << "Node is " << node;
	start_node = node;
    count = 1;
    node = -1;
    maxi = -1;
    for(map<int, vector<int> >::iterator it = graph.begin();it != graph.end();it++){
        marked[it->first] = 0;
    }
    dfs(start_node);
//     cout << "Max is " << maxi<<endl;
// 	cout << "Node is " << node;
    cout << maxi << endl;
	return 0;
}

#DONE