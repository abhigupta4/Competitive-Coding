struct Stack{
	int data;
	Stack* next;
};

void initstack(Stack** head_ref){
	*head_ref = NULL;
}

int empty(Stack* s){
	return (s== NULL);
}

void push(Stack *s,int val){
	Stack* temp = new Stack;
	temp->data = val;
	temp->next = s;
	s = temp;
}

void pop(Stack* s){
	int x;
	Stack* temp = s;
	x = s->data;
	s = s->next;
	free(temp);
	return x;
}

int top(Stack* s){
	return s->data;
}

void sorted_insert(Stack** s,int val){
	if(empty(*s) or val > top(*s)){
		push(*s,val);
	}
	int temp = pop(*s);
	sorted_insert(s,val);
	push(*s,temp);
}

void sort_stack(Stack** s){
	if(empty(*s)){
		return;
	}
	int temp = pop(*s);
	sort_stack(s);
	sorted_insert(s,temp);
}