import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Genre, Title 을 관리하는 영화 데이터베이스.
 * 
 * MyLinkedList 를 사용해 각각 Genre와 Title에 따라 내부적으로 정렬된 상태를  
 * 유지하는 데이터베이스이다. 
 */
public class MovieDB {
	MyLinkedList<MovieDBItem> results;

    public MovieDB() {
        // FIXME implement this
    	results = new MyLinkedList<MovieDBItem>();
    	// HINT: MovieDBGenre 클래스를 정렬된 상태로 유지하기 위한 
    	// MyLinkedList 타입의 멤버 변수를 초기화 한다.
    }

    public <T> void insert(MovieDBItem item) {
        // FIXME implement this
        // Insert the given item to the MovieDB.
		Node<MovieDBItem> check=results.head;
		if(results.size()==0){
			results.add(item);
		}
		for(int i=0; i <=results.size()-1; i++){
			int compare = item.compareTo(check.getNext().getItem());
			check=check.getNext();
			if(compare<0){
				results.insertnext(item, i);
				break;
			}
			else if(compare==0){
				//이미 있는 것이므로 추가하지 않는다.
				break;
			}

			if(i==results.size()-1){
				//끝까지 진행되면 마지막에 추가
				results.add(item);
				break;
			}
		}
		
    	// Printing functionality is provided for the sake of debugging.
        // This code should be removed before submitting your work.
        // System.err.printf("[trace] MovieDB: INSERT [%s] [%s]\n", item.getGenre(), item.getTitle());
    }

    public void delete(MovieDBItem item) {
        // FIXME implement this
        // Remove the given item from the MovieDB.
    	Node<MovieDBItem> check=results.head;
		for(int i=0;i<=results.size()-1;i++){
			int compare = item.compareTo(check.getNext().getItem());
			check=check.getNext();
			if(compare==0){
				results.removenext(i);
			}
		}

    	// Printing functionality is provided for the sake of debugging.
        // This code should be removed before submitting your work.
        // System.err.printf("[trace] MovieDB: DELETE [%s] [%s]\n", item.getGenre(), item.getTitle());
    }

    public MyLinkedList<MovieDBItem> search(String term) {
        // FIXME implement this
        // Search the given term from the MovieDB.
        // You should return a linked list of MovieDBItem.
        // The search command is handled at SearchCmd class.
    	
    	// Printing search results is the responsibility of SearchCmd class. 
    	// So you must not use System.out in this method to achieve specs of the assignment.
    	
        // This tracing functionality is provided for the sake of debugging.
        // This code should be removed before submitting your work.
    	// System.err.printf("[trace] MovieDB: SEARCH [%s]\n", term);
    	
    	// FIXME remove this code and return an appropriate MyLinkedList<MovieDBItem> instance.
    	// This code is supplied for avoiding compilation error.   
        // MyLinkedList<MovieDBItem> results = new MyLinkedList<MovieDBItem>();
		// 순서대로 찾는 영화 이름을 출력
		// 제목에 검색어
		MyLinkedList<MovieDBItem> searchresults = new MyLinkedList<MovieDBItem>();

		Node<MovieDBItem> check=results.head;

		for(int i=0; i<=results.size()-1;i++){
			boolean contain = check.getNext().getItem().getTitle().contains(term);
			check=check.getNext();
			if(contain){
				searchresults.add(check.getItem());
			}
		}

        return searchresults;
    }
    
    public MyLinkedList<MovieDBItem> items() {
        // FIXME implement this
        // Search the given term from the MovieDatabase.
        // You should return a linked list of QueryResult.
        // The print command is handled at PrintCmd class.

    	// Printing movie items is the responsibility of PrintCmd class. 
    	// So you must not use System.out in this method to achieve specs of the assignment.

    	// Printing functionality is provided for the sake of debugging.
        // This code should be removed before submitting your work.
        // System.err.printf("[trace] MovieDB: ITEMS\n");

    	// FIXME remove this code and return an appropriate MyLinkedList<MovieDBItem> instance.
    	// This code is supplied for avoiding compilation error.   
        //MyLinkedList<MovieDBItem> results = new MyLinkedList<MovieDBItem>();
        
    	return results;
    }
}

class Genre extends Node<String> implements Comparable<Genre> {
	public Genre(String name) {
		super(name);
		throw new UnsupportedOperationException("not implemented yet");
	}
	
	@Override
	public int compareTo(Genre o) {
		
		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public int hashCode() {

		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public boolean equals(Object obj) {

		throw new UnsupportedOperationException("not implemented yet");
	}
}

class MovieList implements ListInterface<String> {	
	public MovieList() {
	}

	@Override
	public Iterator<String> iterator() {

		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public boolean isEmpty() {

		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public int size() {

		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public void add(String item) {

		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public String first() {

		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public void removeAll() {
		
		throw new UnsupportedOperationException("not implemented yet");
	}
}