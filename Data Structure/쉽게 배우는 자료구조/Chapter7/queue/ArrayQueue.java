package queue;

public class ArrayQueue<E> implements QueueInterface<E> {
    private E queue[];
    private int front,tail,numItems;
    private static final int DEAULT_CAPACITY=64;
    private final E ERROR = null;

    public ArrayQueue(){
        queue=(E[]) new Object[DEAULT_CAPACITY];
        front= 0;
        tail= DEAULT_CAPACITY-1;
        numItems=0;
    }

    public ArrayQueue(int n){
        queue=(E[]) new Object[n];
        front= 0;
        tail= n-1;
        numItems=0;
    }

    //알고리즘 7-1 구현: 큐에 원소 삽입하기
    public void enqueue(E newItem){
        if(isFull()){
            System.out.println("Queue Full");
        }
        else{
            tail=(tail+1)%queue.length;
            queue[tail]=newItem;
            ++numItems;
        }
    }

    //알고리즘 7-2 구현: 큐가 꽉 찾는지 확인하기
    public boolean isFull(){
        return(numItems==queue.length);
    }

    //알고리즘 7-3 구현: 큐에 원소 삭제하기
    public E dequeue(){
        if(isEmpty()){
            return ERROR;
        }
        else{
            E queueFront = queue[front];
            front = (front+1)%queue.length;
            --numItems;
            return queueFront;
        }
    }

    //알고리즘 7-5 구현: 큐의 맨앞 원소 알려주기
    public E front(){
        if(isEmpty()){
            return ERROR;
        }
        else{
            return queue[front];
        }
    }

    //알고리즘 7-4 구현: 큐가 비었는지 확인하기
    public boolean isEmpty(){
        return (numItems==0);
    }

    //알고리즘 7-5 구현: 큐 비우기
    public void dequeueAll(){
        queue=(E[]) new Object[queue.length];
        front =0;
        tail = queue.length -1;
        numItems =0;
    }
}
