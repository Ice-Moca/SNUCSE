package bst;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TreePrinter<Key extends Comparable<? super Key>, E> {

	public TreePrinter() {
	}

	/**
	 * Given the root of a tree, draw its figure.
	 * @param root
	 */
	public void printNode(BinaryNode<Key, E> root) {
		if (root == null)
			System.out.println("The tree is empty");
		else {
			int maxLevel = maxLevel(root);
			printNodeInternal(Collections.singletonList(root), 1, maxLevel);
		}
	}

	private void printNodeInternal(List<BinaryNode<Key, E>> nodes, int level, int maxLevel) {
		if (nodes.isEmpty() || isAllElementsNull(nodes)) {
			return;
		}

		int floor = maxLevel - level;
		int endgeLines = (int) Math.pow(2, (Math.max(floor - 1, 0)));
		int firstSpaces = (int) Math.pow(2, (floor)) - 1;
		int betweenSpaces = (int) Math.pow(2, (floor + 1)) - 1;

		TreePrinter.printWhitespaces(firstSpaces);

		List<BinaryNode<Key, E>> newNodes = new ArrayList<BinaryNode<Key, E>>();
		for (BinaryNode<Key, E> node : nodes) {
			if (node != null) {
				String bookName = node.getKey().toString();
				String[] nameList = bookName.split("_");
				String shortName = "";
				for (String s : nameList) {
					shortName += s.substring(0, 1);
				}
				System.out.print(shortName+node.getSize());
//				System.out.print(node.getKey().toString());
				newNodes.add(node.getLeft());
				newNodes.add(node.getRight());
			} else {
				newNodes.add(null);
				newNodes.add(null);
				System.out.print(" ");
			}

			TreePrinter.printWhitespaces(betweenSpaces);
		}
		System.out.println("");

		for (int i = 1; i <= endgeLines; i++) {
			for (int j = 0; j < nodes.size(); j++) {
				TreePrinter.printWhitespaces(firstSpaces - i);
				if (nodes.get(j) == null) {
					TreePrinter.printWhitespaces(endgeLines + endgeLines + i + 1);
					continue;
				}

				if (nodes.get(j).getLeft() != null)
					System.out.print("/");
				else
					TreePrinter.printWhitespaces(1);

				TreePrinter.printWhitespaces(i + i - 1);

				if (nodes.get(j).getRight() != null)
					System.out.print("\\");
				else
					TreePrinter.printWhitespaces(1);

				TreePrinter.printWhitespaces(endgeLines + endgeLines - i);
			}

			System.out.println("");
		}

		printNodeInternal(newNodes, level + 1, maxLevel);
	}

	private static void printWhitespaces(int count) {
		for (int i = 0; i < count; i++)
			System.out.print(" ");
	}

	private int maxLevel(BinaryNode<Key, E> node) {
		if (node == null)
			return 0;
		
		return Math.max(maxLevel(node.getLeft()), maxLevel(node.getRight())) + 1;
	}

	private boolean isAllElementsNull(List<BinaryNode<Key, E>> list) {
		for (Object object : list) {
			if (object != null)
				return false;
		}
		return true;
	}
}
