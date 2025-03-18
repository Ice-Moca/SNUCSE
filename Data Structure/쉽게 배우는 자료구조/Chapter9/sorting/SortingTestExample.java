import sorting.Sorting;

public class SortingTestExample {
    public static void main(String[] args) {
        int[] testArray = {5, 2, 9, 1, 5, 6};

        System.out.println("Selection Sort:");
        int[] selectionArray = testArray.clone();
        Sorting selectionSort = new Sorting(selectionArray);
        selectionSort.selectionSort();
        printArray(selectionArray);

        System.out.println("Bubble Sort:");
        int[] bubbleArray = testArray.clone();
        Sorting bubbleSort = new Sorting(bubbleArray);
        bubbleSort.bubbleSort();
        printArray(bubbleArray);

        System.out.println("Insertion Sort:");
        int[] insertionArray = testArray.clone();
        Sorting insertionSort = new Sorting(insertionArray);
        insertionSort.insertionSort();
        printArray(insertionArray);

        System.out.println("Merge Sort:");
        int[] mergeArray = testArray.clone();
        Sorting mergeSort = new Sorting(mergeArray);
        mergeSort.mergeSort();
        printArray(mergeArray);

        System.out.println("Quick Sort:");
        int[] quickArray = testArray.clone();
        Sorting quickSort = new Sorting(quickArray);
        quickSort.quickSort();
        printArray(quickArray);

        System.out.println("Heap Sort:");
        int[] heapArray = testArray.clone();
        Sorting heapSort = new Sorting(heapArray);
        heapSort.heapSort();
        printArray(heapArray);

        System.out.println("Shell Sort:");
        int[] shellArray = testArray.clone();
        Sorting shellSort = new Sorting(shellArray);
        shellSort.shellSort();
        printArray(shellArray);

        System.out.println("Counting Sort:");
        int[] countingArray = testArray.clone();
        Sorting countingSort = new Sorting(countingArray);
        int max = findMax(countingArray); 
        int[] sortedCountingArray = countingSort.countingSort(max + 1);
        printArray(sortedCountingArray);

        System.out.println("Radix Sort:");
        int[] radixArray = testArray.clone();
        Sorting radixSort = new Sorting(radixArray);
        radixSort.radixSort();
        printArray(radixArray);

        System.out.println("Bucket Sort:");
        int[] bucketArray = testArray.clone();
        Sorting bucketSort = new Sorting(bucketArray);
        bucketSort.bucketSort();
        printArray(bucketArray);
    }

    private static void printArray(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    private static int findMax(int[] array) {
        int max = array[0];
        for (int num : array) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }
}