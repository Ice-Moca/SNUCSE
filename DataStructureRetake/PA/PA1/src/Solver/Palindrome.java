package Solver;

import Structures.Queue;
import Structures.Stack;

public class Palindrome {
    private Queue queue;
    private Stack stack;
    private int length;
    private int maxLen; // Store the maximum length

    public Palindrome(int max_len) {
        this.queue = new Queue(max_len);
        this.stack = new Stack(max_len);
        this.length = 0;
        this.maxLen = max_len; // Initialize maxLen
    }

    public void newInt(int i) {
        if (i != 0) { // Ignore zeros
            this.queue.enqueue(i); // Add to the queue
            this.stack.push(i);    // Add to the stack
            this.length++;         // Increment the length
        }
    }

    public void clear() {
        this.queue.clear();
        this.stack.clear();
        // Reset length to 0 in clear method
        this.length = 0; 
    }

    public int length() {
        return this.length;
    }

    public boolean palindromeCheck() {
        int len = this.queue.length(); // Store the current length
        boolean isPalindrome = true;
    
        // Compare elements from the queue and stack
        for (int j = 0; j < len; j++) {
            int queueVal = this.queue.dequeue(); // Remove from the front of the queue
            int stackVal = this.stack.pop();     // Remove from the top of the stack
            if (queueVal != stackVal) {
                isPalindrome = false; // If any mismatch, it's not a palindrome
            }
            if (queueVal == -1 || stackVal == -1) { 
                isPalindrome = false; 
            }
        }
    
        // If not a palindrome, set length to maxLen
        if (!isPalindrome) {
            this.length = this.maxLen;
        }
        this.queue.clear();
        this.stack.clear();
    
        return isPalindrome;
    }
}