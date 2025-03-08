import java.io.*;
import java.util.*;

public class SortingTest
{
	public static void main(String args[])
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		try
		{
			boolean isRandom = false;	// 입력받은 배열이 난수인가 아닌가?
			int[] value;	// 입력 받을 숫자들의 배열
			String nums = br.readLine();	// 첫 줄을 입력 받음
			if (nums.charAt(0) == 'r')
			{
				// 난수일 경우
				isRandom = true;	// 난수임을 표시

				String[] nums_arg = nums.split(" ");

				int numsize = Integer.parseInt(nums_arg[1]);	// 총 갯수
				int rminimum = Integer.parseInt(nums_arg[2]);	// 최소값
				int rmaximum = Integer.parseInt(nums_arg[3]);	// 최대값

				Random rand = new Random();	// 난수 인스턴스를 생성한다.

				value = new int[numsize];	// 배열을 생성한다.
				for (int i = 0; i < value.length; i++)	// 각각의 배열에 난수를 생성하여 대입
					value[i] = rand.nextInt(rmaximum - rminimum + 1) + rminimum;
			}
			else
			{
				// 난수가 아닐 경우
				int numsize = Integer.parseInt(nums);

				value = new int[numsize];	// 배열을 생성한다.
				for (int i = 0; i < value.length; i++)	// 한줄씩 입력받아 배열원소로 대입
					value[i] = Integer.parseInt(br.readLine());
			}

			// 숫자 입력을 다 받았으므로 정렬 방법을 받아 그에 맞는 정렬을 수행한다.
			while (true)
			{
				int[] newvalue = (int[])value.clone();	// 원래 값의 보호를 위해 복사본을 생성한다.
                char algo = ' ';

				if (args.length == 4) {
                    return;
                }

				String command = args.length > 0 ? args[0] : br.readLine();

				if (args.length > 0) {
                    args = new String[4];
                }
				
				long t = System.currentTimeMillis();
				switch (command.charAt(0))
				{
					case 'B':	// Bubble Sort
						newvalue = DoBubbleSort(newvalue);
						break;
					case 'I':	// Insertion Sort
						newvalue = DoInsertionSort(newvalue);
						break;
					case 'H':	// Heap Sort
						newvalue = DoHeapSort(newvalue);
						break;
					case 'M':	// Merge Sort
						newvalue = DoMergeSort(newvalue);
						break;
					case 'Q':	// Quick Sort
						newvalue = DoQuickSort(newvalue);
						break;
					case 'R':	// Radix Sort
						newvalue = DoRadixSort(newvalue);
						break;
					case 'S':	// Search
						algo = DoSearch(newvalue);
						break;
					case 'X':
						return;	// 프로그램을 종료한다.
					default:
						throw new IOException("잘못된 정렬 방법을 입력했습니다.");
				}
				if (isRandom)
				{
					// 난수일 경우 수행시간을 출력한다.
					System.out.println((System.currentTimeMillis() - t) + " ms");
				}
				else
				{
					// 난수가 아닐 경우 정렬된 결과값을 출력한다.
                    if (command.charAt(0) != 'S') {
                        for (int i = 0; i < newvalue.length; i++) {
                            System.out.println(newvalue[i]);
                        }
                    } else {
                        System.out.println(algo);
                    }
				}

			}
		}
		catch (IOException e)
		{
			System.out.println("입력이 잘못되었습니다. 오류 : " + e.toString());
		}
	}

	////////////////////////////////////////////////////////////////////////////////////////////////////
	private static int[] DoBubbleSort(int[] value)
	{
		// value는 정렬안된 숫자들의 배열이며 value.length 는 배열의 크기가 된다.
		// 결과로 정렬된 배열은 리턴해 주어야 하며, 두가지 방법이 있으므로 잘 생각해서 사용할것.
		// 주어진 value 배열에서 안의 값만을 바꾸고 value를 다시 리턴하거나
		// 같은 크기의 새로운 배열을 만들어 그 배열을 리턴할 수도 있다.
		boolean swapped;
		int temp;
		for(int i = 1; i < value.length; i++)
		{
		   swapped = false;
		   for(int j = 0; j < value.length - i; j++)
		   {
			  if(value[j] > value[j+1])
			  {
				 temp = value[j];
				 value[j] = value[j+1];
				 value[j+1] = temp;
				 swapped = true;
			  }
		   }
		   if(!swapped)
		   {
			  break;
		   }
		}
		return (value);
	 }
  

	////////////////////////////////////////////////////////////////////////////////////////////////////
	private static int[] DoInsertionSort(int[] value)
	{
		for (int i = 1; i < value.length; i++) {
		   int key = value[i];
		   int j = i - 1;
	 
		   while (j >= 0 && value[j] > key) {
			  value[j + 1] = value[j];
			  j = j - 1;
		   }
  
		   value[j + 1] = key;
		}
		return value;
	 }
  

	////////////////////////////////////////////////////////////////////////////////////////////////////
	// Heap Sort Algorithm
	private static int[] DoHeapSort(int[] value) {
		int n = value.length;
		
		// Build a max heap
		for (int i = n / 2 - 1; i >= 0; i--) {
			heapify(value, n, i);
		}

		// Extract elements one by one from the heap
		for (int i = n - 1; i > 0; i--) {
			// Swap the root (largest) with the last element
			int temp = value[0];
			value[0] = value[i];
			value[i] = temp;

			// Heapify the reduced heap
			heapify(value, i, 0);
		}
		
		return value;
	}

	// Heapify function to maintain the heap property
	private static void heapify(int[] value, int n, int i) {
		int largest = i;
		int left = 2 * i + 1; // Left child index
		int right = 2 * i + 2; // Right child index

		// If left child is larger than root
		if (left < n && value[left] > value[largest]) {
			largest = left;
		}

		// If right child is larger than largest so far
		if (right < n && value[right] > value[largest]) {
			largest = right;
		}

		// If largest is not the root, swap and continue heapifying
		if (largest != i) {
			int temp = value[i];
			value[i] = value[largest];
			value[largest] = temp;

			// Recursively heapify the affected subtree
			heapify(value, n, largest);
		}
	}


	////////////////////////////////////////////////////////////////////////////////////////////////////
	private static int[] DoMergeSort(int[] value) {
		int[] temp = new int[value.length];
		mergeSort(value, 0, value.length - 1, temp);
		return value;
	}
	
	// Recursive mergeSort function
	private static void mergeSort(int[] value, int left, int right, int[] temp) {
		if (left < right) {
			int middle = (left + right) / 2;
			
			// Recursively sort both halves
			mergeSort(value, left, middle, temp);
			mergeSort(value, middle + 1, right, temp);
			
			// Merge the sorted halves
			merge(value, left, right, temp);
		}
	}
	
	// Merge function to combine two sorted halves
	private static void merge(int[] value, int left, int right, int[] temp) {
		int middle = (left + right) / 2;
		int leftPointer = left, rightPointer = middle + 1, tempPointer = 0;
	
		// Merge the two sorted halves into temp
		while (leftPointer <= middle && rightPointer <= right) {
			if (value[leftPointer] <= value[rightPointer]) {
				temp[tempPointer++] = value[leftPointer++];
			} else {
				temp[tempPointer++] = value[rightPointer++];
			}
		}
	
		// Copy the remaining elements from the left half (if any)
		while (leftPointer <= middle) {
			temp[tempPointer++] = value[leftPointer++];
		}
	
		// Copy the remaining elements from the right half (if any)
		while (rightPointer <= right) {
			temp[tempPointer++] = value[rightPointer++];
		}
	
		// Copy the merged result back to the original array
		System.arraycopy(temp, 0, value, left, right - left + 1);
	}

	////////////////////////////////////////////////////////////////////////////////////////////////////
	private static int[] DoQuickSort(int[] value) {
		quickSort(value, 0, value.length - 1);
		return value;
	}
	
	// Recursive quickSort function
	private static void quickSort(int[] value, int low, int high) {
		if (low < high) {
			// Partition the array and get the pivot index
			int pi = partition(value, low, high);
	
			// Recursively sort elements before and after partition
			quickSort(value, low, pi - 1);
			quickSort(value, pi + 1, high);
		}
	}
	
	// Partition the array around the pivot
	private static int partition(int[] value, int low, int high) {
		int pivot = value[high];  // Pivot element (last element)
		int i = low - 1;          // Index of smaller element
	
		// Traverse through the array
		for (int j = low; j < high; j++) {
			if (value[j] <= pivot) {
				i++;  // Increment index of smaller element
	
				// Swap value[i] and value[j]
				int temp = value[i];
				value[i] = value[j];
				value[j] = temp;
			}
		}
	
		// Swap the pivot element with the element at index i + 1
		int temp = value[i + 1];
		value[i + 1] = value[high];
		value[high] = temp;
	
		// Return the index of the pivot element
		return i + 1;
	}

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// Radix Sort Algorithm
	private static int[] DoRadixSort(int[] value) {
		int max = findMax(value);
		
		// Perform counting sort for every digit (exp is 10^i)
		for (int exp = 1; max / exp > 0; exp *= 10) {
			countSort(value, exp);
		}
	
		return value;
	}
	
	// Find the maximum absolute value in the array
	private static int findMax(int[] value) {
		int max = Math.abs(value[0]);
		for (int i = 1; i < value.length; i++) {
			if (Math.abs(value[i]) > max) {
				max = Math.abs(value[i]);
			}
		}
		return max;
	}
	
	// Counting sort for each digit (based on exp)
	private static void countSort(int[] value, int exp) {
		int n = value.length;
		int[] output = new int[n];
		int[] count = new int[19];  // To handle digits from -9 to 9
		
		// Count occurrences of each digit
		for (int i = 0; i < n; i++) {
			int digit = (value[i] / exp) % 10 + 9;  // Adjust index to handle negative values
			count[digit]++;
		}
	
		// Update count[] to contain actual positions of digits
		for (int i = 1; i < 19; i++) {
			count[i] += count[i - 1];
		}
	
		// Build the output array by placing elements at the correct position
		for (int i = n - 1; i >= 0; i--) {
			int digit = (value[i] / exp) % 10 + 9;  // Get digit and adjust index
			output[count[digit] - 1] = value[i];
			count[digit]--;
		}
	
		// Copy the sorted elements back to the original array
		System.arraycopy(output, 0, value, 0, n);
	}
 
	////////////////////////////////////////////////////////////////////////////////////////////////////
    private static char DoSearch(int[] value)
	{
		int kmd = 5;
      double kcr = 0.2;
      double ksr = 0.8;

      if (maxDigits(value) <= kmd) return 'R'; // maxDigits() 함수로 최대 자릿수 체크
      if (collisionRate(value) >= kcr) return 'H'; // collisionRate() 함수로 중복 비율 체크
      if (sortedRatio(value) >= ksr) return 'I'; // sortedRatio() 함수로 정렬 비율 체크

      return 'Q'; // 기본값
	}
	private static int maxDigits(int[] value) {
		int max = 0;
		for (int num : value) {
		   max = Math.max(max, (int) Math.log10(Math.abs(num) + 1) + 1);
		}
		return max;
	 }
  
	 private static double collisionRate(int[] value) {
		int collisions = 0;
		java.util.HashSet<Integer> uniqueSet = new java.util.HashSet<>();
		for (int num : value) {
		   if (!uniqueSet.add(num)) collisions++; // 중복된 숫자가 있을 때 카운트
		}
		return (double) collisions / value.length;
	 }
  
	 private static double sortedRatio(int[] value) {
		int sortedCount = 0;
		for (int i = 0; i < value.length - 1; i++) {
		   if (value[i] <= value[i + 1]) sortedCount++; // 이전 값보다 크거나 같으면 정렬된 것으로 판단
		}
		return (double) sortedCount / (value.length - 1);
	 }
}
