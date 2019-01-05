#include <bits/stdc++.h>

using namespace std;


struct node{
	int data;
	node* next;
};

void push(node** head_ref,int val){
	node* pt1 = new node;
	pt1->data = val;
	node* temp = *head_ref;
	pt1->next = *head_ref;
	//IF list not empty
	if(*head_ref != NULL){
		while (temp->next != *head_ref)
            temp = temp->next;
        temp->next = pt1;
	}
	//if empty
	else
		pt1->next = pt1;
	*head_ref = pt1;
}

void print(node *head){
	node* temp = head;
	if(head != NULL){
		do{
			printf("%d",&temp->data);
			temp = temp->next;
		}
		while(temp != head);
	}
}

int main(){

	return 0;
}