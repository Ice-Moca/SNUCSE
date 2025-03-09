package bst;

public class BinarySearchTree implements IndexInterfaace<TreeNode>{
    private TreeNode root;
    public BinarySearchTree(){
        root=null;
    }

    //알고리즘 10-1 구현: 검색
    public TreeNode search(Comparable searchKey){
        return searchItem(root,searchKey);
    }

    private TreeNode searchItem(TreeNode tNode, Comparable searchKey){
        if(tNode==null){return null;}
        else if(searchKey.compareTo(tNode.key)==0){return tNode;}
        else if(searchKey.compareTo(tNode.key)<0){return searchItem(tNode.left,searchKey);}
        else{return searchItem(tNode.right,searchKey);}
    }

    //알고리즘 10-2 구현: 삽입
    public void insert(Comparable newKey){
        root = insertItem(root,newKey);
    }

    private TreeNode insertItem(TreeNode tNode, Comparable newItem){
        if(tNode == null){
            tNode= new TreeNode(newItem);
        }
        else if(newItem.compareTo(tNode.key)<0){
            tNode.left = insertItem(tNode.left, newItem);
        }
        else{
            tNode.right = insertItem(tNode.right, newItem);
        }
        return tNode;
    }

    //알고리즘 10-3 구현: 삭제
    public void delete(Comparable searchKey){
        root= deleteItem(root,searchKey);
    }

    private TreeNode deleteItem(TreeNode tNode, Comparable searchKey){
        if(tNode == null){return null;}
        else{
            if(searchKey==tNode.key){
                tNode = deleteNode(tNode);
            }
            else if(searchKey.compareTo(tNode)<0){
                tNode.left=deleteItem(tNode.left, searchKey);
            }
            else{
                tNode.right = deleteItem(tNode.right, searchKey);
            }
            return tNode;
        }
    }

    private TreeNode deleteNode(TreeNode tNode){
        //3 case
        //1. tNode가 리프 노드
        //2. tNode가 자식이 하나만 있음
        //3. tNode가 자식이 둘 있음
        if((tNode.left==null)&&(tNode.right==null)){
            return null;
        }
        else if(tNode.left==null){
            return tNode.right;
        }
        else if(tNode.right==null){
            return tNode.left;
        }
        else{
            returnPair rPair = deleteMinItem(tNode.right);
            tNode.key=rPair.key;
            tNode.right=rPair.node;
            return tNode;
        }
    }

    private returnPair deleteMinItem(TreeNode tNode){
        if(tNode.left==null){
            return new returnPair(tNode.key, tNode.right);
        }
        else{
            returnPair rPair = deleteMinItem(tNode.left);
            tNode.left=rPair.node;
            rPair.node=tNode;
            return rPair;
        }
    }

    private class returnPair{
        private Comparable key;
        private TreeNode node;
        private returnPair(Comparable it, TreeNode nd){
            key = it;
            node= nd;
        }
    }

    //알고리즘 10-4 구현: 기타
    public boolean isEmpty(){
        return root == null;
    }

    public void clear(){
        root=null;
    }
}
