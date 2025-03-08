public class SelectionSort {

    // Selection Sort 알고리즘 구현
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        
        // 배열의 각 원소에 대해
        for (int i = 0; i < n - 1; i++) {
            // i부터 n-1까지의 원소 중에서 최소값을 찾기
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j; // 더 작은 값을 찾으면 그 인덱스로 갱신
                }
            }
            
            // i와 minIndex의 원소를 교환
            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }

    // 배열을 출력하는 함수
    public static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11}; // 예시 배열
        
        System.out.println("Original array:");
        printArray(arr);
        
        // Selection Sort 실행
        selectionSort(arr);
        
        System.out.println("Sorted array:");
        printArray(arr);
    }
}
