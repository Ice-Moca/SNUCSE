import list.LinkedList;
import list.Node;
import bst.IndexInterface;

public class ChainedHashTable implements IndexInterface{
    private java.util.LinkedList<E> table;   
    int numItems=0;

    public ChainedHashTable(int n){
        table=(LinkedList<Integer>[]) new LinkedList[n];
        for(int i=0;i<n;i++){
            table[i]= new LinkedList<>();
        }
        numItems=0;
    }

    private int hash(Integer x){
        return x%table.length; //간단한 버전의 해시테이블
    }    

    //알고리즘 12-1 구현: 검색, 삽입, 삭제
    public void insert(Integer x){
        int slot = hash(x);
        table[slot].add(0,x);
        numItems++;
    }

    public Node search(Integer x){
        int slot = hash(x);
        if(tabel[slot].isEmpty()){return null;}
        else{
            int i= table[slot].indexOf(x);
            if(i==LinkedList.NOT_FOUND){return null;}
            else{return table[slot].getNode();}
        }
    }

    public void delete(Integer x){
        if(isEmpty()){//error
        }
        else{
            int slot=hash(x);
            if(table[slot]==x){
                table[slot].removeItem(x);
                numItems--;
            }
        }
    }

    //기타
    public boolean isEmpty(){
        return numItems=0;
    }

    public void clear(){
        for(int i=0;i<table.length;i++){
            table[i]= new LinkedList<>();
        }
        numItems=0;
    }
}
