package queue;
import list.Node;

public class LinkedQueue<E> implements QueueInterface<E> {
    private Node<E> tail;
    private final E ERROR =null;
    
    public  LinkedQueue(){
        tail=null;
    }

    //알고리즘 7-7 구현: 큐에 원소 추가하기
    public void enqueue(E newItem){
        Node<E> newNode = new Node<>(newItem);
        if(isEmpty()){
            newNode.next=newNode;
            tail=newNode;
        }
        else{
            newNode.next=tail.next;
            tail.next =newNode;
            tail=newNode;
        }
    }

    //알고리즘 7-8 구현: 큐에 원소 삭제하기
    public E dequeue(){
        if(isEmpty()){
            return ERROR;
        }
        else{
            Node<E> front = tail.next;
            if(front==tail){
                tail=null;
            }
            else{
                tail.next=front.next;
            }
            return front.item;
        }
    }
    
    //알고리즘 7-9 구현: 큐의 맨앞 원소 알려주기
    public E front(){
        if(isEmpty()){return ERROR;}
        else{return tail.next.item;}
    }

    //알고리즘 7-10 구현: 큐 비었는지 확인하기
    public boolean isEmpty(){
        return tail==null;
    }

    //알고리즘 7-11 구현: 큐 비우기
    public void dequeueAll(){
        tail=null;
    }
}
