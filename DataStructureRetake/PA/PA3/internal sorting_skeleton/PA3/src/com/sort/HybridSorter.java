package com.sort;


public class HybridSorter<K extends Comparable<? super K>> {
	InsertionSorter<K> insertionSort = new InsertionSorter<K>();
	private final int RUN = 32;
	/**
	 * Sorts the elements in given array from `left` to `right in lexicographic order
	 * using the hybrid sorting algorithm.
	 */

	public Pair<K, ?> search(Pair<K,?>[] array, int k, String sortType) {
		// Fill your code to find k-th element in `array`.
        if (k < 0 || k >= array.length) {
            return null;
        }
        sort(array, 0, array.length - 1, sortType);
        return array[k];
	}
	
	public void sort(Pair<K, ?>[] array, int left, int right, String sortType) {
		// Fill your code to sort the elements in `array`.
		boolean reverse = false;
        String pureSortType = sortType;

        if (sortType.startsWith("sortrev ")) {
            reverse = true;
            pureSortType = sortType.substring("sortrev ".length());
        }

        quicksort(array, left, right, pureSortType, reverse);
	}

	// Hint: Maybe you need to create the helper methods such as partitioning.
	private void quicksort(Pair<K, ?>[] array, int left, int right, String sortType, boolean reverse) {
        if (right - left + 1 <= RUN) {
            insertionSort.sort(array, left, right, sortType, reverse);
            return;
        }
        if (left < right) {
            int pivotIndex = partition(array, left, right, sortType, reverse);
            quicksort(array, left, pivotIndex - 1, sortType, reverse);
            quicksort(array, pivotIndex + 1, right, sortType, reverse);
        }
    }   


    private int partition(Pair<K, ?>[] array, int left, int right, String sortType, boolean reverse) {
        Pair<K, ?> pivot = array[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (compare(array[j], pivot, sortType, reverse) <= 0) {
                i++;
                swap(array, i, j);
            }
        }
        swap(array, i + 1, right);
        return i + 1;
    }


    private int compare(Pair<K, ?> a, Pair<K, ?> b, String sortType, boolean reverse) {
        int cmp = 0;
        if ("keys".equals(sortType)) {
            cmp = a.getKey().compareTo(b.getKey());
        } 
        else if ("values".equals(sortType)) {
            Integer valA = (Integer) a.getValue();
            Integer valB = (Integer) b.getValue();
            cmp = valA.compareTo(valB);
        }
        return reverse ? -cmp : cmp;
    }

    private void swap(Pair<K, ?>[] array, int i, int j) {
        Pair<K, ?> temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    
    @SuppressWarnings("unchecked")
	public Pair<K, ?>[] median(Pair<K, ?>[] array, int size, String sortType) {
        if (size == 0) {
            return (Pair<K, ?>[]) new Pair[0];
        }
        // Copy the array to avoid modifying the original
        Pair<K, ?>[] copy = (Pair<K, ?>[]) new Pair[size];
        System.arraycopy(array, 0, copy, 0, size);

        // Sort the copy of the array
        sort(copy, 0, size - 1, getPureSortType(sortType));

        if (size % 2 == 1) {
            // Odd number of elements: return the middle element
            Pair<K, ?>[] result = (Pair<K, ?>[]) new Pair[1];
            result[0] = copy[size / 2];
            return result;
        } else {
            // Even number of elements: return the two middle elements
            Pair<K, ?>[] result = (Pair<K, ?>[]) new Pair[2];
            result[0] = copy[size / 2 - 1];
            result[1] = copy[size / 2];
            return result;
        }
    }

    // If sortType is "sortrev keys" change it to "keys"
    private String getPureSortType(String sortType) {
        if (sortType == null) return "";
        if (sortType.startsWith("sortrev ")) {
            return sortType.substring("sortrev ".length());
        }
        return sortType;
    }
}
