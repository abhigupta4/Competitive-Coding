#include <bits/stdc++.h>
using namespace std;

struct Queue{
	int front,rear,size;
	unsigned capacity;
	int* array;
};

struct Queue* createQueue(unsigned capacity)
{
    Queue* queue = new Queue;
    queue->capacity = capacity;
    queue->front = queue->size = 0; 
    queue->rear = capacity - 1;  // This is important, see the enqueue
    queue->array = new int[capacity];
    return queue;
}
 
// Queue is full when size becomes equal to the capacity 
int isFull(Queue* queue)
{  return (queue->size == queue->capacity);  }
 
// Queue is empty when size is 0
int isEmpty(Queue* queue)
{  return (queue->size == 0); }
 
// Function to add an item to the queue.  It changes rear and size
void enqueue(Queue* queue, int item)
{
    if (isFull(queue))
        return;
    queue->rear = (queue->rear + 1)%queue->capacity;
    queue->array[queue->rear] = item;
    queue->size = queue->size + 1;
    printf("%d enqueued to queue\n", item);
}
 
// Function to remove an item from queue.  It changes front and size
int dequeue(Queue* queue)
{
    if (isEmpty(queue))
        return INT_MIN;
    int item = queue->array[queue->front];
    queue->front = (queue->front + 1)%queue->capacity;
    queue->size = queue->size - 1;
    return item;
}

int front(Queue* queue)
{
    if (isEmpty(queue))
        return INT_MIN;
    return queue->array[queue->front];
}
 
// Function to get rear of queue
int rear(Queue* queue)
{
    if (isEmpty(queue))
        return INT_MIN;
    return queue->array[queue->rear];
}
 
// Driver program to test above functions./
int main()
{
    Queue* queue = createQueue(1000);
 
    enqueue(queue, 10);
    enqueue(queue, 20);
    enqueue(queue, 30);
    enqueue(queue, 40);
 
    printf("%d dequeued from queue\n", dequeue(queue));
 
    printf("Front item is %d\n", front(queue));
    printf("Rear item is %d\n", rear(queue));
 
    return 0;
}