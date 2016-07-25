#include <bits/stdc++.h>
#include <stdio.h>
 
using namespace std;
 
long int max(long int a,long int b){
	if (a > b){
		return a;
	}
	return b;
}
 
struct node{
	long int lmax,rmax,tot,max;
};
 
void build(vector<node> &st,int arr[],int idx, int start, int end){
    if(start == end){
    	st[idx].lmax = st[idx].rmax = st[idx].tot = st[idx].max = arr[start];
    	return;
    }
    int mid = (start + end) / 2;
    int le = 2*idx+1;
    int ri = 2*idx+2;
    build(st,arr,le, start, mid);
    build(st,arr,ri, mid+1, end);
    st[idx].tot = st[le].tot + st[ri].tot;
    st[idx].lmax = max(st[le].lmax,st[le].tot + st[ri].lmax);
    st[idx].rmax = max(st[ri].rmax,st[ri].tot + st[le].rmax);
    int temp = max(st[ri].max,st[le].rmax+st[ri].lmax);
    st[idx].max = max(st[idx].rmax,max(st[idx].lmax,max(st[le].max,temp)));
} 
 
node query(vector<node> &tree,int index, int start, int end, int l, int r)
{
    if(r < start or end < l){
		node temp;
		temp.lmax = temp.rmax = temp.tot = temp.max = -66000;
        return temp;
    }
    if(l <= start and end <= r)
    {
        return tree[index];
    }
    int mid = (start + end) / 2;
    node left = query(tree,2*index+1, start, mid, l, r);
    node right = query(tree,2*index+2, mid+1, end, l, r);
    node temp;
    temp.tot = left.tot + right.tot;
    temp.lmax = max(left.lmax,left.tot + right.lmax);
    temp.rmax = max(right.rmax,right.tot + left.rmax);
    long int tempo = max(right.max,left.rmax+right.lmax);
    temp.max = max(temp.rmax,max(temp.lmax,max(left.max,tempo)));
    return temp;
}

int main()
{
	int n,m,l,r;
	scanf("%d",&n);
	vector<node> tree(1000000);
	int array[100001];
	for(int i=1;i<=n;i++)
		scanf("%d",&array[i]);
    scanf("%d",&m);
	build(tree,array,0,1,n);
 
	while(m--)
	{
		scanf("%d %d",&l,&r);
		node temp=query(tree,0,1,n,l,r);
		printf("%d\n",(temp.max));
	}
	return 0;
}  