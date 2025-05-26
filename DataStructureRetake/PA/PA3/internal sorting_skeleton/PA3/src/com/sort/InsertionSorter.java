package com.sort;

public class InsertionSorter<K extends Comparable<? super K>> {

	/**
	 * Sorts the elements in given array from `left` to `right` in lexicograph order using insertion sort algorithm.
	 */
	
	public void sort(Pair<K, ?>[] array, int left, int right, String sortType, boolean reverse) {
		// Fill your code to sort the elements in `array`.
		for (int i = left + 1; i <= right; i++) {
            Pair<K, ?> key = array[i];
            int j = i - 1;

            while (j >= left && compare(array[j], key, sortType, reverse) > 0) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
		
	}


	// Hint: Maybe you need to create the helper methods to swap elements.
	private int compare(Pair<K, ?> a, Pair<K, ?> b, String sortType, boolean reverse) {
        int cmp = 0;
        if (sortType.equals("keys")) {
            // Key comparsion (K is Comparable)
            cmp = a.getKey().compareTo(b.getKey());
        } 
        else if (sortType.equals("values")) {
            // Value comparsion (Set Integer typ)
            Integer valA = (Integer) a.getValue();
            Integer valB = (Integer) b.getValue();
            cmp = valA.compareTo(valB);
        }

        return reverse ? -cmp : cmp;
    }
	

}