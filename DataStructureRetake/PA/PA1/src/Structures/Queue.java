package Structures;

public class Queue {
    private int[] queue;    // Array to store queue elements
    private int front;      // Index of the front element
    private int rear;       // Index of the rear element
    private int size;       // Current size of the queue
    private int capacity;   // Capacity of the queue

    public Queue(int max_len) {
        this.capacity = max_len;
        this.queue = new int[max_len];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    public void clear() {
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    public boolean isempty() {
        return this.size == 0;
    }

    public int length() {
        return this.size;
    }

    public void enqueue(int val) {
        if (this.size == this.capacity) {
            return; 
            // an exception, queue is full
            // due to main function, with throws IOException
            // I didn't handle the exception here
        }
        this.rear = (this.rear + 1) % this.capacity;
        this.queue[this.rear] = val;
        this.size++;
    }

    public int dequeue() {
        if (this.isempty()) {
            return -1; // an exception
        }
        int val = this.queue[this.front];
        this.front = (this.front + 1) % this.capacity;
        this.size--;
        return val;
    }
}