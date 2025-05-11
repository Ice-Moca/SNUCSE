package bst;

import java.util.ArrayList;
import java.util.List;

public class BookSearch {
	
	private BinarySearchTree<String, String> bst;

	/**
	 * Constructor 
	 * Do not modify this function.
	 */
	public BookSearch() {
		bst = new BinarySearchTree<>();
	}

	/**
	 * This function returns the root of the bst.
	 * TreePrinter will call this function to print your current tree.
	 * So do not modify this function.
	 * @return the root of the BinarySearchTree
	 */
	public BinaryNode<String, String> getRoot() {
		if (bst == null)
			return null;
		return bst.getRoot();
	}

	/**
	 * This function adds the book information into BookSearch.
	 * The book information is in forms of a key-value pair: 
	 * the key is "name" as the book name, and the value is "location" of the book.
	 * @param name of the book
	 * @param position of the book
	 */
	public void add(String name, String position) {
		///TODO: Fill in this function
        bst.insert(name, position);
	}

	/**
	 * This function removes the book with "name" from BookSearch.
	 * @param name of the book we want to remove.
	 * @return the location of removed book. If no such book, return null.
	 */
	public String remove(String name) {
		///TODO: Fill in this function
		return bst.remove(name);
	}

	/**
	 * Given the book name, this function should return the location of the book.  
	 * @param name of the book that we want to get.
	 * @return the position of the book. If no such book, return null.
	 */
	public String get(String name) {
		///TODO: Fill in this function
        return bst.find(name);
	}

	/**
	 * This function returns the number of books in the BookSearch.
	 * @return the number of books.
	 */
	public int size() {
		///TODO: Fill in this function
        return bst.size();
	}

	/**
	 * This function retrieves the information of books in lexicographical order. 
	 * The function should print all book names. Print each book name for each line. 
	 * The Output specification is "BOOK:\t"+ bookName.
	 * If BookSearch does not have any book, print the message "BookSearch does not have any book".
	 */
	public void printBookList() {
		///TODO: Fill in this function
        bst.printBookList();
	}

	/**
	 * This function finds the name of the book of the given order.
	 * @param order of the book.
	 * @return the name of corresponding book.
	 */
	public String orderSearch(int order){
		///TODO: Fill in this function
        return bst.orderSearch(order);
	}

	/**
	 * This function finds the order of the book of the given name.
	 * @param name of the book.
	 * @return the order of the book.
	 */
	public int orderSearch(String name){
		///TODO: Fill in this function
        return bst.orderSearch(name);
	}

	/**
     * This function determines whether the bst is valid or not.
     *
     * @return validation result.
     */
	public boolean validationCheck(){
		///TODO: Fill in this function
        return bst.validationCheck();
	}

	/**
     * Finds all keys which start with the given prefix,
     * in lexicographical order.
     * @return a list of keys which start with the given prefix 
     */
	public List<String> prefixSearch(String prefix) {
		///TODO: Fill in this function
        return bst.prefixSearch(prefix);
	}

	/**
     * This function prints whether the tree is balanced (balance factor ≤ 1)
     * or needs to be rebalanced (balance factor > 1).
     */
	public void balanceCheck() {
		///TODO: Fill in this function
        bst.balanceCheck();
	}

	/**
     * This function finds all keys whose associated location values start with the given section prefix,
     * in lexicographical (in-order) order.
     *
     * @return a list of keys (book names) whose stored location strings start with the section prefix
     */
	public List<String> locationSearch(String section) {
		///TODO: Fill in this function
		return bst.locationSearch(section);
	}

}
