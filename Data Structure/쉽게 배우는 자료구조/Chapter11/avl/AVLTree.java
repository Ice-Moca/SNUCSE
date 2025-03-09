package avl;

import bst.IndexInterfaace;

public class AVLTree implements IndexInterfaace<AVLNode>{
    private AVLNode root;
    static final AVLNode NIL=new AVLNode(null,null,null,0);

    public AVLTree(){
        root=NIL;
    }
    
    private final int LL=1,LR=2,RR=3,RL=4,NO_NEED=0,ILLEGAL=-1;
    private int needBalance(AVLNode t){
        int type = ILLEGAL;
        if(t.left.height+2<=t.right.right.height){
            if((t.right.left.height)<=t.right.right.height){
                type=RR;
            }
            else{
                type=RL;
            }
        }
        else if((t.left.height)>=t.right.height+2){
            if((t.left.left.height)>=t.left.right.height){
                type=LL;
            }
            else{
                type=LR;
            }
        }
        else{
            type=NO_NEED;
        }
        return type;
        
    }

    //알고리즘 10-1구현: 검색
    public AVLNode search(Comparable x){
        return searchItem(root,x);
    }

    private AVLNode searchItem(AVLNode tNode,Comparable x){
        if(tNode==NIL){return NIL;}
        else if(x.compareTo(tNode.item)==0){return tNode;}
        else if(x.compareTo(tNode.item)< 0){return searchItem(tNode.left,x);}
        else{return searchItem(tNode.right,x);}
    }

    //알고리즘 10-2 구현: 삽입
    public void insert(Comparable x){
        root = insertItem(root,x);
    }

    private AVLNode insertItem(AVLNode tNode, Comparable x){
        if(tNode==NIL){
            tNode= new AVLNode(x);
        }
        else if(x.compareTo(tNode.item)<0){
            tNode.left=insertItem(tNode.left,x);
            tNode.height=1+Math.max(tNode.right.height,tNode.left.height);
            int type = needBalance(tNode);
            if(type != NO_NEED){
                tNode = balanceAVL(tNode,type);
            }
        }
        else{
            tNode.right=insertItem(tNode.right, x);
            tNode.height=1+Math.max(tNode.right.height,tNode.left.height);
            int type = needBalance(tNode);
            if(type!=NO_NEED){
                tNode=balanceAVL(tNode,type);
            }
        }
        return tNode;
    }

    //알고리즘 10-3 구현: 삭제
    public void delete(Comparable x){
        root = deleteItem(root,x);
    }

    private AVLNode deleteItem(AVLNode tNode, Comparable x){
        if(tNode==NIL){return NIL;}
        else{
            if(x.compareTo(tNode.item)==0){
                tNode=deleteNode(tNode);
            }
            else if(x.compareTo(tNode.item)<0){
                tNode.left=deleteItem(tNode.left, x);
                tNode.height=1+Math.max(tNode.right.height,tNode.left.height);
                int type = needBalance(tNode);
                if(type!=NO_NEED){
                    tNode=balanceAVL(tNode,type);
                }
            }
            else{
                tNode.right=deleteItem(tNode.right, x);
                tNode.height=1+Math.max(tNode.right.height,tNode.left.height);
                int type= needBalance(tNode);
                if(type!=NO_NEED){
                    tNode=balanceAVL(tNode,type);
                }
            }
            return tNode;
        }
    }

    private AVLNode deleteNode(AVLNode tNode){
        //3 case
        //1. tNode가 리프 노드
        //2. tNode가 자식이 하나만 있음
        //3. tNode가 자식이 둘 있음
        if((tNode.left==NIL)&&(tNode.right==NIL)){
            return null;
        }
        else if(tNode.left==NIL){
            return tNode.right;
        }
        else if(tNode.right==NIL){
            return tNode.left;
        }
        else{
            returnPair rPair = deleteMinItem(tNode.right);
            tNode.item=rPair.item;
            tNode.right=rPair.node;
            tNode.height=1+Math.max(tNode.right.height,tNode.left.height);
            int type  = needBalance(tNode);
            if(type!=NO_NEED){
                tNode=balanceAVL(tNode,type);
            }
            return tNode;
        }
    }

    
    private returnPair deleteMinItem(AVLNode tNode){
        int type;
        if(tNode.left==NIL){
            return new returnPair(tNode.item, tNode.right);
        }
        else{
            returnPair rPair = deleteMinItem(tNode.left);
            tNode.left=rPair.node;
            tNode.height=1+Math.max(tNode.right.height,tNode.left.height);
            type=needBalance(tNode);
            if(type!=NO_NEED){
                tNode=balanceAVL(tNode,type);
            }
            rPair.node=tNode;
            return rPair;
        }
    }

    private class returnPair{
        private Comparable item;
        private AVLNode node;
        private returnPair(Comparable it, AVLNode nd){
            item = it;
            node= nd;
        }
    }

    //균형잡기
    private AVLNode balanceAVL(AVLNode tNode, int type){
        AVLNode returnNode = NIL;
        switch(type){
            case LL:
                returnNode=rightRotate(tNode);
                break;
            case LR:
                tNode.left = leftRotate(tNode.left);
                returnNode = rightRotate(tNode);
                break;
            case RR:
                returnNode = leftRotate(tNode);
                break;
            case RL:
                tNode.right = rightRotate(tNode.right);
                returnNode = leftRotate(tNode);
                break;
            default:
                System.out.println("Impossible type! Should be one of LL,LR,RR,RL");
                break;
        }
        return returnNode;
    }
    
    
    //알고리즘 11-1 구현: 좌회전
    private AVLNode leftRotate(AVLNode t){
        AVLNode RChild=t.right;
        if(RChild==NIL){
            System.out.println(t.item+"'s RChild shouldn't be NIL!");
        }
        AVLNode RLChild = RChild.left;
        RChild.left=t;
        t.right=RLChild;
        t.height=1+Math.max(t.left.height,t.right.height);
        RChild.height=1+Math.max(RChild.left.height,RChild.right.height);
        return RChild;
    }
    
    
    //알고리즘 11-1 구현: 우회전
    private AVLNode rightRotate(AVLNode t){
        AVLNode LChild=t.left;
        if(LChild==NIL){
            System.out.println(t.item+"'s LChild shouldn't be NIL!");
        }
        AVLNode LRChild = LChild.left;
        LChild.right=t;
        t.left=LRChild;
        t.height=1+Math.max(t.left.height,t.right.height);
        LChild.height=1+Math.max(LChild.left.height,LChild.right.height);
        return LChild;
    }
    
    //기타
    public boolean  isEmpty(){
        return root==NIL;
    }

    public void clear(){
        root=NIL;
    }
}
