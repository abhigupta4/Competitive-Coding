#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int i,index,test,number,unique;
	scanf("%d",&test);
	index = test; 
	long long int array[test];
	while (test > 0){
		scanf("%u",&array[index - test]);
		test--;
	}
	array[index] = '\0';
	i = 0;
	unique = 0;
	while( array[i] != '\0'){
		unique = unique ^ array[i];
		i++;
	}
	printf("%u",unique);
	return 0;
}

//DONE