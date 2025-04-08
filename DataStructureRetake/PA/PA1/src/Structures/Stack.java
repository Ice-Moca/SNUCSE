package Structures;

public class Stack {
    private int[] stack;    // Array to store stack elements
    private int top;        // Index of the top element
    private int capacity;   // Capacity of the stack

    public Stack(int max_len) {
        this.capacity = max_len;
        this.stack = new int[max_len];
        this.top = -1;
    }

    public void clear() {
        this.top = -1;
    }

    public boolean isempty() {
        return this.top == -1;
    }

    public int length() {
        return this.top + 1;
    }

    public void push(int val) {
        if (this.top == this.capacity - 1) {
            return; 
            // an exception, stack is full
            // no value is pushed to the stack
        }
        this.top++;
        this.stack[this.top] = val;
    }

    public int pop() {
        if (this.isempty()) {
            return -1;
            // an exception, stack is empty
            // no value is popped from the stack
            // return -1 which is not positive int
        }
        this.top--;
        return this.stack[this.top+1];
    }
}