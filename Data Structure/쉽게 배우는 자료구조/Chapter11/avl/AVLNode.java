package avl;

public class AVLNode {
    public Comparable item;
    public AVLNode left,right;
    public int height;
    
    public AVLNode(Comparable newItem){
        item = newItem;
        left=right=AVLTree.NIL;
        height=1;
    }

    public AVLNode(Comparable newItem, AVLNode leftChild, AVLNode rightChild){
        item=newItem;
        left=leftChild;right=rightChild;
        height=1;
    }

    public AVLNode(Comparable newItem, AVLNode leftChild, AVLNode rightChild,int h){
        item=newItem;
        left=leftChild;right=rightChild;
        height=h;
    }
}
