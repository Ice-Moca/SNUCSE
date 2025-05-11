package bst;

import java.util.List;
import java.util.ArrayList;

public class BinarySearchTree<Key extends Comparable<? super Key>, E> {

    /**
     * root of this tree
     */
    private BinaryNode<Key, E> root;
    private int nodeCount = 0;

    // Declare more variables HERE

    /**
     * Constructor
     * Do not modify this function.
     */
    public BinarySearchTree() {
        root = null;
        nodeCount = 0;
    }

    /**
     * This function returns the root of the BST.
     * Do not modify this function.
     *
     * @return root of the BinarySearchTree
     */
    public BinaryNode<Key, E> getRoot() {
        return root;
    }

    /**
     * Reinitialize tree
     */
    public void clear() {
        root = null;
        nodeCount = 0;
    }

    /**
     * Insert an item into the tree.
     *
     * @param key   of the item
     * @param value of the item
     */
    public void insert(Key key, E value) {
        ///TODO: Fill in this function
        /// insert the time <key,value> into the tree
        /// if the key already exists, update its value
        root = insertHelp(root, key, value);
        nodeCount++;
    }

    /**
     * Insert the item <key,value> into the tree rt.
     *
     * @param rt    of the tree.
     * @param key   of the item to be inserted.
     * @param value of the item to be inserted.
     * @return the tree after insertion
     */
    private BinaryNode<Key, E> insertHelp(BinaryNode<Key, E> rt, Key key, E value) {
        ///TODO: Fill in this function
        /// insert the item <key,value> into the tree rt
        /// if the key already exists, update its value
        /// return the tree after insertion
        if (rt == null) {
            return new BinaryNode<Key, E>(key, value);
        }
        int cmp = key.compareTo(rt.getKey());
        if (cmp < 0) {
            rt.setLeft(insertHelp(rt.getLeft(), key, value));
            rt.increaseSize();
        } else if (cmp > 0) {
            rt.setRight(insertHelp(rt.getRight(), key, value));
            rt.increaseSize();
        } else {
            rt.setValue(value);
        }
        return rt;
    }

    /**
     * Remove an item from the tree.
     *
     * @param key of the item to be removed.
     * @return the value of the removed item. If no such item, return null.
     */
    public E remove(Key key) {
        ///TODO: Fill in this function
        /// remove the item with given key from the tree
        /// get null from find if the item does not exist
        E removedValue = find(key);
        if (removedValue != null) {
            root = removeHelp(root, key);
            nodeCount--;
        }
        return removedValue;
    }

    /**
     * Remove a node with given key from the tree rt.
     *
     * @param rt  of the tree.
     * @param key of the item to be removed.
     * @return the tree after removing.
     */
    private BinaryNode<Key, E> removeHelp(BinaryNode<Key, E> rt, Key key) {
        ///TODO: Fill in this function
        /// remove the node with given key from the tree rt
        /// return null if the tree is empty
        if (rt == null) {
            return null;
        }
        int cmp = key.compareTo(rt.getKey());
        if (cmp < 0) {
            rt.setLeft(removeHelp(rt.getLeft(), key));
            rt.decreaseSize();
        } else if (cmp > 0) {
            rt.setRight(removeHelp(rt.getRight(), key));
            rt.decreaseSize();
        } else {
            // Found node to remove
            if (rt.getLeft() == null) {
                return rt.getRight();
            } else if (rt.getRight() == null) {
                return rt.getLeft();
            } else {
                // two children: replace with successor
                BinaryNode<Key, E> succ = getMin(rt.getRight());
                rt.setKey(succ.getKey());
                rt.setValue(succ.getValue());
                rt.setRight(removeHelp(rt.getRight(), succ.getKey()));
                rt.decreaseSize();
            }
        }
        return rt;
    }

    /**
     * Given a tree rt, get its smallest node.
     * The smallest node is the node with the minimum key.
     *
     * @param rt
     * @return the smallest node.
     */
    private BinaryNode<Key, E> getMin(BinaryNode<Key, E> rt) {
        ///TODO: Fill in this function
        /// get the smallest node in the tree rt
        if (rt == null) {
            return null;
        }
        while (rt.getLeft() != null) {
            rt = rt.getLeft();
        }
        return rt;
    }

    /**
     * Given a tree rt, delete the smallest node and return this tree.
     *
     * @param rt is the root of the tree
     * @return the tree after deletion.
     */
    private BinaryNode<Key, E> deleteMin(BinaryNode<Key, E> rt) {
       ///TODO: Fill in this function
       if (rt == null) {
        return null;
        }
        if (rt.getLeft() == null) {
            return rt.getRight();
        }
        rt.setLeft(deleteMin(rt.getLeft()));
        rt.decreaseSize();
        return rt;
    }

    /**
     * Find the item with given key.
     *
     * @param key of the item
     * @return the value if the item. If no such item, return null.
     * Do not modify this function.
     */
    public E find(Key key) {
        return findHelp(root, key);
    }

    /**
     * @return The number of nodes in the tree.
     */
    public int size() {
        return nodeCount;
    }

    /**
     * Find the item with given key in the tree rt.
     *
     * @param rt  is the root of the tree.
     * @param key is the key that we want to find in tree rt.
     * @return the value of the wanted item. If no such item, return null.
     */
    private E findHelp(BinaryNode<Key, E> rt, Key key) {
        ///TODO: Fill in this function
        /// find the item with given key in the tree rt 
        /// if the item does not exist, return null
        if (rt == null) {
            return null;
        }
        int cmp = key.compareTo(rt.getKey());
        if (cmp < 0) {
            return findHelp(rt.getLeft(), key);
        } else if (cmp > 0) {
            return findHelp(rt.getRight(), key);
        } else {
            return rt.getValue();
        }
    }

    /**
     * Prints all keys in the tree in ascending order.
     * Do not modify this function.
     */
    public void printBookList() {
        printBookListHelper(root);
    }

    /**
     * Prints all keys in the tree with given root using inorder traversal.
     *
     * @param rt is the root of the tree. This param is used for the recursion.
     */
    public void printBookListHelper(BinaryNode<Key, E> rt) {
        ///TODO: Fill in this function
        /// print all keys in the tree with given root using inorder traversal
        if (rt == null) {
            return;
        }
        printBookListHelper(rt.getLeft());
        System.out.println("BOOK:\t" + rt.getKey());
        printBookListHelper(rt.getRight());
    }

    /**
     * Given the order of the item, find the key of the corresponding item.
     *
     * @param order is the order of the item
     * @return the key of corresponding item. If no such item, return null.
     */
    public Key orderSearch(int order) {
        ///TODO: Fill in this function
        /// find the key of the item with given order
        if (order <= 0 || order > size()) {
        return null;
        }
        return orderSearchHelper(root, order);
    }

    /**
     * Given the order of the item and rt of the tree,
     * find the key of the corresponding item in the tree.
     *
     * @param rt    is the root of the tree.
     * @param order is the order of the item
     * @return the key of corresponding item. If no such item, return null.
     */
    private Key orderSearchHelper(BinaryNode<Key, E> rt, int order) {
        ///TODO: Fill in this function
        /// find the key of the item with given order
        /// If no such item, return null
        if (rt == null) {
            return null;
        }
        int leftSize = rt.getLeft() == null ? 0 : rt.getLeft().getSize();
        if (order == leftSize + 1) {
            return rt.getKey();
        } else if (order <= leftSize) {
            return orderSearchHelper(rt.getLeft(), order);
        } else {
            return orderSearchHelper(rt.getRight(), order - leftSize - 1);
        }
    }

    /**
     * Given the key of the item, find the order of the item.
     *
     * @param key of the item
     * @return the order of the item. If no such item, return 0.
     */

    public int orderSearch(Key key) {
        ///TODO: Fill in this function
        /// Give 0 if the item does not exist using orederSearchHelper
        return orderSearchHelper(root, key, 0);
    }

    /**
     * Given the key of the item and the root of the tree,
     * find the order of the item in the tree.
     *
     * @param rt    of the tree
     * @param key   of the item
     * @param count is the number of small items found before.
     * @return the order of the item. If no such item, return 0.
     */
    private int orderSearchHelper(BinaryNode<Key, E> rt, Key key, int count) {
        ///TODO: Fill in this function
        /// find the order of the item with given key
        /// If no such item, return 0
        if (rt == null) {
            return 0;
        }
        int cmp = key.compareTo(rt.getKey());
        int leftSize = rt.getLeft() == null ? 0 : rt.getLeft().getSize();
        if (cmp == 0) {
            return count + leftSize + 1;
        } else if (cmp < 0) {
            return orderSearchHelper(rt.getLeft(), key, count);
        } else {
            return orderSearchHelper(rt.getRight(), key, count + leftSize + 1);
        }
    }

    /**
     * compute height of the tree
     * @return height of the tree
     */
    public int height(){
        ///TODO: Fill in this function
        return heightHelper(root);
    }

    /**
     * Given a tree node, compute the height of the subtree
     * under the given node in a recursive way.
     * @param rt: the given node
     * @return height of the subtree
     */
    private int heightHelper(BinaryNode<Key, E> rt){
        ///TODO: Fill in this function
        if (rt == null) {
            return 0;
        }
        return Math.max(heightHelper(rt.getLeft()), heightHelper(rt.getRight())) + 1;
    }

    /**
     * Check whether the tree is valid or not
     * @return validation result
     */
    public boolean validationCheck(){
        ///TODO: Fill in this function
        return validationCheckHelper(root);
    }

    /**
     * Check whether the subtree under the given node
     * is valid or not in a recursive way
     * @param rt: the given node
     * @return validation result
     */
    public boolean validationCheckHelper(BinaryNode<Key, E> rt){
        ///TODO: Fill in this function
        if (rt == null) {
            return true;
        }
        // check left subtree max < rt.key
        if (rt.getLeft() != null) {
            BinaryNode<Key, E> maxNode = rt.getLeft();
            while (maxNode.getRight() != null) {
                maxNode = maxNode.getRight();
            }
            if (maxNode.getKey().compareTo(rt.getKey()) >= 0) {
                return false;
            }
        }
        // check right subtree min > rt.key
        if (rt.getRight() != null) {
            BinaryNode<Key, E> minNode = rt.getRight();
            while (minNode.getLeft() != null) {
                minNode = minNode.getLeft();
            }
            if (minNode.getKey().compareTo(rt.getKey()) <= 0) {
                return false;
            }
        }
        return validationCheckHelper(rt.getLeft()) && validationCheckHelper(rt.getRight());
    }

    /**
     * Finds all keys whose toString() starts with the given prefix,
     * in lexicographical order.
     * @return a list of keys which start with the given prefix 
     */
    public List<Key> prefixSearch(String prefix) {
        ///TODO: Fill in this function
        List<Key> result = new ArrayList<>();
        prefixSearchHelper(root, prefix, result);
        return result;
    }

    /** Store keys starting with the provided prefix into result
    * @param node   the current subtree root to search
    * @param prefix the prefix to match against each key’s string representation
    * @param result the list into which matching keys are accumulated
    */
    private void prefixSearchHelper(BinaryNode<Key, E> node,
                                    String prefix,
                                    List<Key> result) {
        if (node == null) {
            return;
        }
        prefixSearchHelper(node.getLeft(), prefix, result);
        if (node.getKey().toString().startsWith(prefix)) {
            result.add(node.getKey());
        }
        prefixSearchHelper(node.getRight(), prefix, result);
    }

    /**
     * Compute the absolute difference between heights of left and right subtrees.
     * @return the balance factor of the whole tree
     */
    public int getBalanceFactor() {
        ///TODO: Fill in this function
        if (root == null) {
            return 0;
        }
        int leftHeight = heightHelper(root.getLeft());
        int rightHeight = heightHelper(root.getRight());
        return Math.abs(leftHeight - rightHeight);
    }

    /**
     * Print whether the tree is balanced (balance factor ≤ 1)
     * or needs to be rebalanced (balance factor > 1).
     */
    public void balanceCheck() {
        ///TODO: Fill in this function
        int bf = getBalanceFactor();
        if (bf <= 1) {
            System.out.println("The tree is balanced");
        } else {
            System.out.println("The tree needs to be rebalanced.");
        }
    }

    /**
     * Finds all keys whose associated location values start with the given section prefix,
     * in lexicographical (in-order) order.
     *
     * @param section the section prefix to match (e.g., "C1"); any value whose
     *                toString() begins with this prefix will be included
     * @return a list of keys (book names) whose stored location strings start with the section prefix
     */
    public List<Key> locationSearch(String section) {
        ///TODO: Fill in this function
        List<Key> result = new ArrayList<>();
        locationSearchHelper(root, section, result);
        return result;
    }

    /**
     * Recursively traverses the tree in in-order fashion, filtering nodes by
     * whether their location value begins with the given section prefix
     * and collecting the matching keys.
     *
     * @param node    the current subtree root being examined
     * @param section the section prefix to match against each node’s value
     * @param result  the list into which matching keys are accumulated
     */
    private void locationSearchHelper(BinaryNode<Key, E> node,
                                      String section,
                                      List<Key> result) {
        ///TODO: Fill in this function
        if (node == null) {
            return;
        }
        locationSearchHelper(node.getLeft(), section, result);
        if (node.getValue().toString().startsWith(section)) {
            result.add(node.getKey());
        }
        locationSearchHelper(node.getRight(), section, result);
    }
    
    // Implement more functions HERE

}
