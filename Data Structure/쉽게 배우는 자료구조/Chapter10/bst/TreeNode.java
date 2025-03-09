package bst;

public class TreeNode {
    public Comparable key;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(Comparable newKey){
        key= newKey;
        left=right=null;
    }
    public TreeNode(Comparable newKey, TreeNode leftNode, TreeNode rightNode){
        key = newKey;
        left=leftNode;
        right=rightNode;
    }
}
