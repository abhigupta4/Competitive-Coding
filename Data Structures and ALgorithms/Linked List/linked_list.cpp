//Make a linked list of three elements and traverse it till it ends	
#include <bits/stdc++.h>

using namespace std;

struct node{
	int val;
	node *next;
};

void push(node **head_ref,int new_data){
	node *temp = new node;
	temp->val = new_data;
	temp->next = *head_ref;
	*head_ref = temp;
}

void insert_after(node *prev_node,int val){
	node *temp = new node;
	temp->val = val;	
	temp->next = prev_node->next;
	prev_node->next = temp;
}

void insert_at_end(node **head_ref,int val){
	node *temp = new node;
	temp->val = val;
	temp->next = NULL;
	node *start = new node;
	start = *head_ref
	while(start->next != NULL){
		start = start->next;
	}
	start->next = temp;
	return;
}

void delete_node(node** head_ref,int key){
	node* temp;
	temp = *head_ref;
	if (temp != NULL and temp->val == key){
		*head_ref = temp->next;
		free(temp);
		return;
	}
	node* prev;
	while(temp != NULL and temp->val != key){
		prev = temp;
		temp = temp->next;
	}
	if (temp == NULL){
		return;
	}
	else{
		prev->next = temp->next;
		free(temp);
	}
}
void delete_pos(node** head_ref,int pos){
	node* temp = *head_ref;
	if(temp == NULL){
		return;
	}
	if(pos == 0){
		*head_ref = temp->next;
		free(temp);
		return;
	}
	for(int i=0;temp != NULL and i<pos-1;i++){
		temp = temp->next;
	}

	if(temp == NULL or temp->next == NULL){
		return;
	}
	node* t1 = temp->next->next; 
	free(temp->next);
	temp->next = t1;
}	

int len_iter(node** head_ref){
	int count = 0;
	node* temp = *head_ref;
	while(temp!= NULL){
		count += 1
		temp = temp->next;
	}
	return count;
}

int len_recur(node *cur){
	if(cur == NULL){
		return 0;
	}
	return 1 + recur(cur->next)
}

bool search_iter(node* head,int val){
	if (head == NULL){
		return false;
	}
	node* temp = head;
	while(temp != NULL){
		if (temp->val == val){
			return true;
		}
		temp = temp->next;
	}
	return false;
}

bool search_recur(node* head,int val){
	if (head == NULL){
		return false;
	}
	if(head->val == val){
		return true;
	}
	return search_recur(head->next,val)
}

void swap_nodes(node** head_ref,int x,int y){
	if(x==y){
		return;
	}
	node *prev1,*curr1;
	prev1 = NULL;
	curr1 = *head_ref;
	while(curr1 != NULL and curr1->val != x){
		prev1 = curr1;
		curr1 = curr1->next;
	}
	node *prev2,*curr2;
	prev2 = NULL;
	curr2 = *head_ref;
	while(curr2 != NULL and curr2->next != y){
		prev2 = curr2;
		curr2 = curr2->next;
	}
	if (curr2 == NULL or curr1 == NULL){
		return;
	}
	if(prev1 != NULL){
		prev1->next = curr2;
	}
	else{
		*head_ref = curr2;
	}

	if(prev2 != NULL){
		prev2->next = curr1;
	}
	else{
		*head_ref = curr1;
	}
	node* temp = curr1->next;
	curr1->next = curr2->next;
	curr2->next = temp;
}

int n_node(node* head,int n){
	int count = 0;
	node* temp = head;
	while(temp != NULL and count < n){
		temp = temp->next;
		count++;
	}
	if(temp != NULL){
		return temp;
	}
	return -1;
}

void reverse(struct node** head_ref)
{
    struct node* prev   = NULL;
    struct node* current = *head_ref;
    struct node* next;
    while (current != NULL)
    {
        next  = current->next;  
        current->next = prev;   
        prev = current;
        current = next;
    }
    *head_ref = prev;
}

void recursiveReverse(struct node** head_ref)
{
    struct node* first;
    struct node* rest;
      
    /* empty list */
    if (*head_ref == NULL)
       return;   
 
    /* suppose first = {1, 2, 3}, rest = {2, 3} */
    first = *head_ref;  
    rest  = first->next;
 
    /* List has only one node */
    if (rest == NULL)
       return;   
 
    /* reverse the rest list and put the first element at the end */
    recursiveReverse(&rest);
    first->next->next  = first;  
     
    /* tricky step -- see the diagram */
    first->next  = NULL;          
 
    /* fix the head pointer */
    *head_ref = rest;              
}

node* merge_sorted(node* a,node* b){
	if(a==NULL){
		return b;
	}
	if(b==NULL){
		return a;
	}
	node* temp;
	if(a->val >= b->val){
		temp = a;
		temp->next = merge_sorted(a->next,b);
	}
	else{
		temp = b;
		temp->next = merge_sorted(b->next,a);
	}
	return result;
}

node* rev_sizeK(node* head,int k){
	node* current = head;
	node* prev = NULL;
	node* next = NULL;
	int count = 0;
	while(current != NULL and count <k){
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
		count++;
	}
	if(next != NULL){
		head->next = rev_sizeK(next,k);
	}
	return prev;
}

struct node* addTwoLists (struct node* first, struct node* second)
{
    struct node* res = NULL; // res is head node of the resultant list
    struct node *temp, *prev = NULL;
    int carry = 0, sum;
 
    while (first != NULL || second != NULL) //while both lists exist
    {
        // Calculate value of next digit in resultant list.
        // The next digit is sum of following things
        // (i)  Carry
        // (ii) Next digit of first list (if there is a next digit)
        // (ii) Next digit of second list (if there is a next digit)
        sum = carry + (first? first->data: 0) + (second? second->data: 0);
 
        // update carry for next calulation
        carry = (sum >= 10)? 1 : 0;
 
        // update sum if it is greater than 10
        sum = sum % 10;
 
        // Create a new node with sum as data
        temp = newNode(sum);
 
        // if this is the first node then set it as head of the resultant list
        if(res == NULL)
            res = temp;
        else // If this is not the first node then connect it to the rest.
            prev->next = temp;
 
        // Set prev for next insertion
        prev  = temp;
 
        // Move first and second pointers to next nodes
        if (first) first = first->next;
        if (second) second = second->next;
    }
 
    if (carry > 0)
      temp->next = newNode(carry);
 
    // return head of the resultant list
    return res;
}

int main(){
	node *head;
	node *second;
	node *third;
	head = new node; 
	second = new node;
	third = new node;
	head->val = 1;
	head->next = second;
	second->val = 2;
	second->next = third;
	third->val = 3;
	third->next = 0;
	node *temp;
	temp = head;
	while(temp != 0){
		cout << temp->val << endl;
		temp = temp->next;
	}
	return 0;
}
