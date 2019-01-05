#include <bits/stdc++.h>

using namespace std;

struct Stack{
	int top;
	unsigned capacity;
	int* array;
};

struct Stack* createStack(unsigned capacity){
	Stack* stack = new Stack;
	stack->top = -1;
	stack->capacity = capacity;
	stack->array = new int[capacity];
	return stack;
}

int full(Stack* stack){
	return stack->top == stack->capacity -1;
}

int empty(Stack* stack){
	return stack->top == -1;
}

void push(Stack* stack,int val){
	if(full(stack)){
		return;
	}
	stack->top++;
	stack->array[stack->top] = val;
}

int pop(Stack* stack){
	if(empty(stack)){
		return INT_MIN;
	}
	return stack->array[stack->array--];
}

int peek(Stack* stack){
	if(empty(stack)){
		return INT_MIN;
	}
	return stack->array[stack->top];
}
int main(){

	return 0;
}