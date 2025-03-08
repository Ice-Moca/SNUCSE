package list;

public class CircularDoublyLinkedList<E> implements ListInterface<E> {
    private BidirectionalNode<E> head;
    private int numItems;

    public CircularDoublyLinkedList(){//생성자자
        numItems =0;
        head = new BidirectionalNode<>(null); //더미헤드
        head.next=head.prev=head;
    }

    public void add(int index, E x){
        if(index >= 0 && index<=numItems){
            BidirectionalNode<E> prevNode= getNode(index-1);
            BidirectionalNode<E> newNode= new BidirectionalNode<>(prevNode,x,prevNode.next);
            newNode.next.prev=newNode;
            prevNode.next = newNode;
            numItems++;
        }
    }

    public void append(E x){
        BidirectionalNode<E> prevNode=head.prev;
        BidirectionalNode<E> newNode = new BidirectionalNode<>(prevNode,x,head);
        prevNode.next=newNode;
        head.prev=newNode;
        numItems++;
    }

    //알고리즘 5-12 구현: 리스트에 원소 삭제제하기
    public E remove(int index){ //tail remove
        if(index >= 0 && index<= numItems-1){
            BidirectionalNode<E> currNode= getNode(index);
            currNode.prev.next=currNode.next;
            currNode.next.prev=currNode.prev;
            numItems--;
            return currNode.item;
        }
        else{
            return null;
        }
    }

    public boolean removeItem(E x){
        BidirectionalNode<E> currNode=head; //더미헤드
        for(int i=0;i<=numItems-1;i++){
            currNode = currNode.next;
            if(((Comparable)(currNode.item)).compareTo(x)==0){
                currNode.prev.next=currNode.next;
                currNode.next.prev=currNode.prev;
                numItems--;
                return true;
            }
        }
        return false; //Not found
    }

    public E get(int index){
        if(index>=0 && index<=numItems -1){
            return getNode(index).item;
        }
        else{
            return null; //에러
        }
    }

    public BidirectionalNode<E> getNode(int index){
        if(index>=-1 && index<=numItems-1 ){
            BidirectionalNode<E> currNode = head;
            if(index<numItems/2){
                for(int i=0;i<=index;i++){
                    currNode= currNode.next;
                }
            }
            else{
                for(int i= numItems-1;i>=index;i--){
                    currNode=currNode.prev;
                }
            }
            return currNode;
        }
        else{
            return null;
        }
    }

    //알고리즘 5-14 구현: 연결 리스트의 k번째 원소를 x로 대체하기
    public void set(int index, E x){
        if(index>=0 && index<=numItems-1){
            getNode(index).item=x;
        }
    }

    //알고리즘 5-15 구현: 원소 x가 연결 리스트의 몇 번째 원소인지 알려주기
    public final int NOT_FOUND=-12345;
    public int indexOf(E x){
        BidirectionalNode<E> currNode = head;
        for(int i=0;i<numItems;i++){
            currNode=currNode.next;
            if(((Comparable)(currNode.item)).compareTo(x)==0){
                return i;
            }
        }
        return NOT_FOUND;
    }
    
    //알고리즘 5-16(1) 구현: 리스트의 총 원소 수 알려주기
    public int len(){
        return numItems;
    }

    //알고리즘 5-16(2) 구현: 리스트의 비었는지지 알려주기
    public boolean isEmpty(){
        return numItems==0;
    }

    //알고리즘 5-16(3) 구현: 리스트비우기
    public void clear(){
        numItems=0;
        head.next=head.prev=head;
    }
}
