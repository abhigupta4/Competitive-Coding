#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define F first
#define S second
#define sd(a) scanf("%d",&a)
#define sdl(a) scanf("%lld",&a)
#define pd(a) printf("%d\n",a)
#define pdl(a) printf("%lld\n",a)
#define mp make_pair
#define pb push_back
#define FOR(i, a, n) for(int i = (a); i < (n); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define MOD 1000000007
#define pii pair<int,int> 

map<int,vector<int> > comp;
vector<pii> sock;

int adap[212345];
int conn[212345];

int main(){
	int n,m,val;	
	int temp,pow1,index,yolo;
	sd(n);sd(m);
	
	REP(i,n){
		sd(val);
		comp[val].pb(i);
	}

	REP(i,m){
		sd(val);
		sock.pb(mp(val,i));
	}
	sort(sock.begin(),sock.end());
	
	int c=0,u=0;
	REP(i,sock.size()){
		temp = 0;
		pow1 = sock[i].F;
		index = sock[i].S;
		while(pow1 > 0){
			if (comp[pow1].size()){
				yolo = comp[pow1][comp[pow1].size()-1];
				comp[pow1].pop_back();
				conn[yolo] = index+1;
				adap[index] = temp;
				c++;
				u += temp;
				break;
			}
			if (pow1 == 1){
				break;
			}
			pow1 = (pow1+1)/2;
			temp++;
		}
	}
	cout << c << " " << u << endl;
	REP(i,m){
		cout << adap[i] << " ";
	}
	cout << endl;
	REP(i,n){
		cout << conn[i] << " ";
	}
	cout << endl;
	return 0;
}