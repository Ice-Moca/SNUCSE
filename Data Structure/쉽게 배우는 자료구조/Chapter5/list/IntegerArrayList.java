package list;

public class IntegerArrayList implements IntegerListInterface{
    private Integer[] item;
    private int numItems;
    private static final int DEFAULT_CAPACITY=64;

    public IntegerArrayList(){//생성자 1
        item= new Integer[DEFAULT_CAPACITY];
        numItems =0;
    }

    public IntegerArrayList(int n){//생성자 2
        item= new Integer[n];
        numItems =0;
    }

    //알고리즘 5-1 구현: 배열 리스트의 k번째 자리에 원소 x 삽입하기
    public void add(int index, Integer x){
        if(numItems>=item.length||index<0||index>numItems){
            //에러처리
        }
        else{
            for(int i=numItems-1;i>=index;i--){
                item[i+1] = item[i]; //item 오른쪽으로 밀기
            }
            item[index]=x;
            numItems++;
        }
    }

    //알고리즘 5-2 구현: 배열 리스트의 맨 뒤에 원소 추가하기
    public void append(Integer x){
        if(numItems>=item.length){
            //에러 처리
        }
        else{
            item[numItems++] = x;
            //인덱스 numItems에 새로운 값을 할당 후 numItems값 증가, 후중연산자
        }
    }
    
    //알고리즘 5-3 구현: 배열 리스트의 k번째 원소 삭제하기
    public Integer remove(int index){
        if(isEmpty()||index<0||index>numItems-1){
            return null;
        }
        else{
            Integer tmp = item[index];
            for(int i=index;i<numItems-2;i++){
                item[i]=item[i+1];//item 왼쪽으로 밀기기
            }
            numItems--;
            return tmp;        
        }
    }

    //알고리즘 5-4 구현: 배열 리스트에서 원소 x 삭제하기
    public boolean removeItem(Integer x){
        int k=0;
        while(k<numItems && item[k].compareTo(x)!=0){
            k++;
        }
        if(numItems==k){
            return false;
        }
        else{
            for(int i=k;i<=numItems-2;i++){
                item[i]=item[i+1]; //좌시프트
            }
            numItems--;
            return true;
        }
    }

    //알고리즘 5-5 구현: 배열 리스트의 i번쨰 원소 알려주기
    public Integer get(int index){ //첫번째 원소 0번째로 표기
        if(index>=0&&index<=numItems-1){
            return item[index];
        }
        else{
            return null;
        }
    }

    //알고리즘 5-6 구현: 배열 리스트의 i번째 원소를 x로 대체하기
    public void set(int index, Integer x){
        if(index>=0&&index<=numItems-1){
            item[index]=x;
        }
    }

    //알고리즘 5-7 구현: 원소 x가 배열 리스트의 몇번째 원소인지 알려주기
    private final int NOT_FOUND = -12345;
    public int indexOf(Integer x){
        int i =0;
        for(i=0; i<numItems;i++){
            if((item[i]).compareTo(x)==0){
                return i;
            }
        }
        return NOT_FOUND;
    }

    //알고리즘 5-8(1) 구현: 배열 리스트의 총원소수 알려주기
    public int len(){
        return numItems;
    }

    //알고리즘 5-8(2) 구현: 배열 리스트의 비었는지지 알려주기
    public boolean isEmpty(){
        return numItems==0;
    }
    
    //알고리즘 5-8(3) 구현: 배열 리스트 개끗이 청소하기
    public void clear(){
        numItems=0;
        item=new Integer[item.length];
    }

}