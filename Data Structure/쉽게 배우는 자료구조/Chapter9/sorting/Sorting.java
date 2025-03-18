package sorting;

import java.util.LinkedList;

public class Sorting {
    int A[];
    public Sorting(int[] B){
        A = B;
    }

    // Selection Sort
    public void selectionSort(){
        int k; int tmp;
        for(int last = A.length - 1; last >= 1; last--){
            k = theLargest(last); // Find the largest element in the unsorted part
            tmp = A[k]; A[k] = A[last]; A[last] = tmp; // Swap the largest element with the last element
        }
    }

    private int theLargest(int last){
        int largest = 0;
        for(int i = 0; i <= last; i++){
            if(A[i] > A[largest]){ largest = i; } // Update the index of the largest element
        }
        return largest;
    }

    // Bubble Sort
    public void bubbleSort(){
        int tmp = 0;
        boolean swapped;
        for(int last = A.length - 1; last >= 2; last--){
            swapped = false;
            for(int i = 0; i <= last - 1; i++){
                if(A[i] > A[i + 1]){
                    tmp = A[i];
                    A[i] = A[i + 1];
                    A[i + 1] = tmp; // Swap adjacent elements if they are in the wrong order
                    swapped = true;
                }
            }
            if(!swapped){ break; } // If no swaps occurred, the array is already sorted
        }
    }

    // Insertion Sort
    public void insertionSort(){
        for(int i = 1; i <= A.length - 1; i++){
            int loc = i - 1;
            int newItem = A[i];
            while(loc >= 0 && newItem < A[loc]){
                A[loc + 1] = A[loc]; // Shift elements to the right
                loc--;
            }
            A[loc + 1] = newItem; // Insert the new item in the correct position
        }
    }

    // Merge Sort
    public void mergeSort(){
        int[] B = new int[A.length];
        mSort(0, A.length - 1, B);
    }

    private void mSort(int p, int r, int[] B){
        if(p < r){
            int q = (p + r) / 2;
            mSort(p, q, B); // Sort the left half
            mSort(q + 1, r, B); // Sort the right half
            merge(p, q, r, B); // Merge the two halves
        }
    }

    private void merge(int p, int q, int r, int[] B){
        int i = p;
        int j = q + 1;
        int t = 0;
        while(i <= q && j <= r){
            if(A[i] <= A[j]){
                B[t++] = A[i++];
            } else {
                B[t++] = A[j++];
            }
        }
        while(i <= q){
            B[t++] = A[i++];
        }
        while(j <= r){
            B[t++] = A[j++];
        }
        i = p; t = 0;
        while(i <= r){
            A[i++] = B[t++];
        }
    }

    // Quick Sort
    public void quickSort(){
        qSort(0, A.length - 1);
    }

    private void qSort(int p, int r){
        if(p < r){
            int q = partition(p, r); // Partition the array
            qSort(p, q - 1); // Sort the left part
            qSort(q + 1, r); // Sort the right part
        }
    }

    private int partition(int p, int r){
        int x = A[r];
        int i = p - 1;
        int tmp;
        for(int j = p; j <= r - 1; j++){
            if(A[j] <= x){
                i++;
                tmp = A[i]; A[i] = A[j]; A[j] = tmp; // Swap elements
            }
        }
        tmp = A[i + 1]; A[i + 1] = A[r]; A[r] = tmp; // Place the pivot in the correct position
        return i + 1;
    }

    // Heap Sort
    public void heapSort(){
        buildHeap(); // Build a max heap
        int tmp;
        for(int i = A.length - 1; i >= 1; i--){
            tmp = A[0];
            A[0] = A[i];
            A[i] = tmp; // Swap the root with the last element
            percolateDown(0, i - 1); // Restore the heap property
        }
    }

    public void buildHeap(){
        if(A.length >= 2){
            for(int i = (A.length - 2) / 2; i >= 0; i--){
                percolateDown(i, A.length - 1);
            }
        }
    }

    private void percolateDown(int i, int n){
        int leftChild = 2 * i + 1;
        int rightChild = 2 * i + 2;
        if(leftChild <= n){
            if(rightChild <= n && A[leftChild] < A[rightChild]){
                leftChild = rightChild;
            }
            if(A[i] < A[leftChild]){
                int tmp = A[i];
                A[i] = A[leftChild];
                A[leftChild] = tmp;
                percolateDown(leftChild, n);
            }
        }
    }

    // Shell Sort
    public void shellSort(){
        for(int h = A.length / 7; h > 5; h = h / 5 - 1){
            for(int k = 0; k <= h - 1; k++){
                stepInsertionSort(k, h);
            }
        }
        stepInsertionSort(0, 1);
    }

    void stepInsertionSort(int k, int h){
        int j, insItem;
        for(int i = k + h; i <= A.length - 1; i += h){
            insItem = A[i];
            for(j = i - h; j >= 0 && A[j] > insItem; j -= h){
                A[j + h] = A[j];
            }
            A[j + h] = insItem;
        }
    }

    // Counting Sort
    public int[] countingSort(int k){ // k is the maximum value in the array
        int[] cnt = new int[k];
        for(int i = 0; i < k; i++){ cnt[i] = 0; } // Initialize the count array
        for(int i = 0; i < A.length; i++){ cnt[A[i]]++; } // Count the occurrences of each element
        for(int i = 1; i < k; i++){ cnt[i] += cnt[i - 1]; } // Compute the cumulative counts
        int[] B = new int[A.length];
        for(int j = A.length - 1; j >= 0; j--){
            B[cnt[A[j]] - 1] = A[j]; // Place elements in the sorted order
            cnt[A[j]]--;
        }
        return B;
    }

    // Radix Sort
    public void radixSort(){
        int[] cnt = new int[10], start = new int[10];
        int[] B = new int[A.length];
        int max = -1;
        for(int i = 0; i < A.length; i++){
            if(A[i] > max){ max = A[i]; }
        }
        int numDigits = (int) Math.log10(max) + 1; // Calculate the number of digits
        for(int digit = 1; digit <= numDigits; digit++){
            for(int d = 0; d <= 9; d++){ cnt[d] = 0; } // Initialize the count array
            for(int i = 0; i < A.length; i++){
                cnt[(int)(A[i] / Math.pow(10, digit - 1)) % 10]++; // Count occurrences of each digit
            }
            start[0] = 0;
            for(int d = 1; d <= 9; d++){
                start[d] = start[d - 1] + cnt[d - 1]; // Compute the starting index for each digit
            }
            for(int i = 0; i < A.length; i++){
                B[start[(int)(A[i] / Math.pow(10, digit - 1)) % 10]++] = A[i]; // Place elements in the sorted order
            }
            for(int i = 0; i < A.length; i++){
                A[i] = B[i]; // Copy the sorted elements back to the original array
            }
        }
    }

    // Bucket Sort
    public void bucketSort() {
        LinkedList<Integer>[] B;
        int numLists = A.length;
        B = new LinkedList[numLists];
        for (int i = 0; i < numLists; i++) {
            B[i] = new LinkedList<>();
        }
    
        // Find the maximum value in the array
        int max = 0;
        for (int i = 1; i < A.length; i++) {
            if (A[i] > A[max]) {
                max = i;
            }
        }
    
        int band = A[max] + 1;
    
        // Distribute elements into buckets
        for (int i = 0; i < A.length; i++) {
            int bucketId = Math.min((int)((float)A[i] / band * numLists), numLists - 1);
            B[bucketId].add(A[i]);
        }
    
        // Collect elements from buckets and sort within each bucket
        int finger = 0;
        for (int i = 0; i < numLists; i++) {
            if (!B[i].isEmpty()) { // Check if the bucket is not empty
                for (int j = 0; j < B[i].size(); j++) {
                    A[finger++] = B[i].get(j);
                }
                rangeInsertionSort(finger - B[i].size(), finger - 1); // Sort elements within the bucket
            }
        }
    }

    private void rangeInsertionSort(int p, int r){
        for(int i = p + 1; i <= r; i++){
            int loc = i - 1;
            int x = A[i];
            while(loc >= p && x < A[loc]){
                A[loc + 1] = A[loc];
                loc--;
            }
            A[loc + 1] = x; // Insert the element in the correct position
        }
    }
}