package heap;

public class Heap<E extends Comparable> implements PQInterface<E> {
    private E[] A;
    private int numItems;

    public Heap(int arraySize){
        A=(E[]) new Comparable[arraySize];
        numItems=0;
    }

    public Heap(E[] B, int numElements){
        A=B;
        numItems=numElements;
    }

    //알고리즘 8-2 구현: 힙에 원소 삽입하기 재귀적 알고리즘
    public void insert(E newItem) throws PQException{
        if(numItems<A.length){
            A[numItems]=newItem;
            percolalteUP(numItems);
            numItems++;
        }
        else{
            throw new PQException("HeapErr: Insert()-Overflow!");
        }
    }

    //스며오르기 percolalteUP()
    private void percolalteUP(int i){
        int parent = (i-1)/2;
        if(parent>=0 && A[i].compareTo(A[parent])>=0){
            E tmp = A[i];
            A[i] = A[parent];
            percolalteUP(parent);
        }
    }

    //알고리즘 8-3 구현: 힙에서 원소 삭제하기
    public E deleteMax() throws PQException{
        if(!isEmpty()){
            E max = A[0];
            A[0] = A[numItems  -1];
            numItems--;
            percolalteDown(0);
            return max;
        }
        else{
            throw new PQException("HeapErr: DeleteMax()-Underflow");
        }
    }

    //스며내리기 percolateDown()
    private void percolalteDown(int i){
        int leftChild = 2*i + 1;
        int rightChild = 2*i + 2;
        if(leftChild<=numItems - 1){
            if(rightChild<=numItems-1 && A[leftChild].compareTo(A[rightChild])<0){
                leftChild = rightChild;
            }
            if(A[i].compareTo(A[leftChild])<0){
                E tmp = A[i];
                A[i] = A[leftChild];
                A[leftChild]=tmp;
                percolalteDown(leftChild);
            }
        }
    }

    //알고리즘 8-4 구현: 힙 만들기
    public void buildHeap(){
        if(numItems>=2){
            for(int i=(numItems-2)/2; i>=0;i--){
                percolalteDown(i);
            }
        }
    }

    //알고리즘 8-5 구현: 힙의 최댓값 구하기
    public E max() throws PQException{
        if(!isEmpty()){
            return A[0];
        }
        else throw new PQException("HeapErr: Max()-Empty!");
    }

    //알고리즘 8-6 구현: 힙이 비었는지 확인하기
    public boolean isEmpty(){
        return numItems ==0;
    }

    //알고리즘 8-7 구현: 힙 비우기
    public void clear(){
        A=(E[])new Object[A.length];
        numItems=0;
    }
}
