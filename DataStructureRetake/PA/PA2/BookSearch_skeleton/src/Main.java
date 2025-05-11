import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.List;

import bst.BookSearch;
import bst.TreePrinter;

public class Main {

	private static final int ADD = 0;
	private static final int REMOVE = 1;
	private static final int GET = 2;
	private static final int SIZE = 3;
	private static final int PRINT_ALL = 4;
	private static final int ORDER_SEARCH = 5;
	private static final int VALIDATION_CHECK = 6;
	private static final int EFFICIENCY_CHECK = 7;
	private static final int PRINT_TREE = 8;
	private static final int PREFIX_SEARCH = 9;
	private static final int BALANCE_CHECK = 10;
	private static final int LOCATION_SEARCH = 11;
	private static final int ERROR = 12;


	public static void main(String[] args) throws Exception {

		if (args.length < 2) {
            System.err.println("Usage: java Main <input_filepath> <output_filepath>");
            System.exit(1);
        }
        String inputFile = args[0];
        String outputFile = args[1];

        // Redirect stdout to the specified output file
        PrintStream fileOut = new PrintStream(new FileOutputStream(outputFile));
        System.setOut(fileOut);

        // Set up input reader
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(new FileInputStream(inputFile)));

		BookSearch bookSearch = new BookSearch();
		TreePrinter<String, String> tp = new TreePrinter<String, String>();

		for (String line = reader.readLine(); line != null; line = reader.readLine()) {
			String[] line_split = line.split(" ");
			String cmd = line_split[0];
			String name = null;
			String position = null;
			String query = null;

			switch (getCommandNum(cmd)) {
			case ADD:
				name = line_split[1];
				position = line_split[2];
				bookSearch.add(name, position);
				System.out.println("ADD:\t" + name + " " + position);
				break;
			case REMOVE:
				name = line_split[1];
				position = bookSearch.remove(name);
				if (name == null || position == null)
					System.out.println("BookSearch cannot find the book");
				else {
					System.out.println("REMOVE:\t" + name +" "+ position);
				}
				break;
			case GET:
				name = line_split[1];
				position = bookSearch.get(name);
				if (position == null)
					System.out.println("BookSearch cannot find the book");
				else
					System.out.println("GET:\t" + name + " " + position);
				break;
			case SIZE:
				System.out.println("SIZE:\t" + bookSearch.size());
				break;
			case PRINT_ALL:
				if (bookSearch.size() ==0)
					System.out.println("BookSearch does not have any book");
				else
					bookSearch.printBookList();
				break;
			case ORDER_SEARCH:
				query = line_split[1];
				if (isNumeric(query)){
					int order = Integer.parseInt(query);
					String result = bookSearch.orderSearch(order);
					if (result == null)
						System.out.println("BookSearch cannot find the book");
					else
						System.out.println("ORDER:\t"+result);
				}else{
					int order = bookSearch.orderSearch(query);
					if (order == 0)
						System.out.println("BookSearch cannot find the book");
					else
						System.out.println("ORDER:\t"+order);
				}
				break;
			case VALIDATION_CHECK:
				if (bookSearch.size() ==0){
					System.out.println("BookSearch does not have any book");
					break;
				}
				boolean isValid = bookSearch.validationCheck();
				if (isValid)
					System.out.println("BookSearch is valid");
				else
					System.out.println("BookSearch is not valid");
				break;
			case PRINT_TREE:
				System.out.println("PRINT_TREE:\t");
				tp.printNode(bookSearch.getRoot());
				break;
			case PREFIX_SEARCH:
				query = line_split[1];
				System.out.println("PREFIX:\t" + query);
				List<String> matches = bookSearch.prefixSearch(query);
				if (matches==null || matches.isEmpty())
					System.out.println("BookSearch cannot find any book starting with \"" + query + "\"");
				else {
					for (String title : matches) {
						System.out.println("BOOK:\t" + title);
					}
				}
				break;
			
			case BALANCE_CHECK:
				// prints directly from the BST:
				bookSearch.balanceCheck();
				break;
			case LOCATION_SEARCH:
				String loc = line_split[1];
				System.out.println("LOCATION:\t" + loc);
				List<String> books = bookSearch.locationSearch(loc);
				if (books==null || books.isEmpty()) {
					System.out.println("BookSearch cannot find any book in section " + loc);
				} else {
					for (String b : books) {
						String bookPos = bookSearch.get(b);
						System.out.println("BOOK:\t" + b + " " + bookPos);
					}
				}
				break;	

			case ERROR:
				break;
		

			}
		}
	}

	private static int getCommandNum(String cmd) {
		if (cmd.equals("add"))
			return ADD;
		else if (cmd.equals("remove"))
			return REMOVE;
		else if (cmd.equals("get"))
			return GET;
		else if (cmd.equals("size"))
			return SIZE;
		else if (cmd.equals("print_all"))
			return PRINT_ALL;
		else if (cmd.equals("order_search"))
			return ORDER_SEARCH;
		else if (cmd.equals("validation_check"))
			return VALIDATION_CHECK;
		else if (cmd.equals("efficiency_check"))
			return EFFICIENCY_CHECK;
		else if (cmd.equals("print_tree"))
			return PRINT_TREE;
		else if (cmd.equals("prefix_search"))
			return PREFIX_SEARCH;
		else if (cmd.equals("balance_check")) 
			return BALANCE_CHECK;
		else if (cmd.equals("location_search")) 
			return LOCATION_SEARCH;	
		return ERROR;
	}

	private static boolean isNumeric(String str){
		try{
			Integer.parseInt(str);
			return true;
		}catch(NumberFormatException e){
			return false;
		}
	}

}
