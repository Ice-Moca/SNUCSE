import java.util.*;

public class AVLTree<T extends Comparable<T>, E> {
    private AVLNode<T, E> root;

    // 삽입
    public void add(T key, E value) {
        root = insert(root, key, value);
    }

    // 전위 순회 반환
    public List<T> getPreorderKeys() {
        List<T> keys = new ArrayList<>();
        traversePreorder(root, keys);
        return keys;
    }

    // 키로 값 검색
    public List<E> findValues(T key) {
        return search(root, key);
    }

    // 삽입 구현
    private AVLNode<T, E> insert(AVLNode<T, E> node, T key, E value) {
        if (node == null) return new AVLNode<>(key, value);

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            node.left = insert(node.left, key, value);
        } else if (cmp > 0) {
            node.right = insert(node.right, key, value);
        } else {
            node.addValue(value);
            return node;
        }

        updateHeight(node);
        return rebalance(node);
    }

    // 검색 구현
    private List<E> search(AVLNode<T, E> node, T key) {
        if (node == null) return Collections.emptyList();

        int cmp = key.compareTo(node.key);
        if (cmp == 0) return node.values;
        if (cmp < 0) return search(node.left, key);
        return search(node.right, key);
    }

    // 높이 업데이트
    private void updateHeight(AVLNode<T, E> node) {
        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));
    }

    // 균형 조정
    private AVLNode<T, E> rebalance(AVLNode<T, E> node) {
        int balance = getHeight(node.left) - getHeight(node.right);

        if (balance > 1) {
            if (getHeight(node.left.left) >= getHeight(node.left.right)) {
                return rotateRight(node); // LL
            } else {
                node.left = rotateLeft(node.left); // LR
                return rotateRight(node);
            }
        }

        if (balance < -1) {
            if (getHeight(node.right.right) >= getHeight(node.right.left)) {
                return rotateLeft(node); // RR
            } else {
                node.right = rotateRight(node.right); // RL
                return rotateLeft(node);
            }
        }

        return node;
    }

    // 높이 반환
    private int getHeight(AVLNode<T, E> node) {
        return (node == null) ? 0 : node.height;
    }

    // 우회전
    private AVLNode<T, E> rotateRight(AVLNode<T, E> y) {
        AVLNode<T, E> x = y.left;
        y.left = x.right;
        x.right = y;

        updateHeight(y);
        updateHeight(x);

        return x;
    }

    // 좌회전
    private AVLNode<T, E> rotateLeft(AVLNode<T, E> x) {
        AVLNode<T, E> y = x.right;
        x.right = y.left;
        y.left = x;

        updateHeight(x);
        updateHeight(y);

        return y;
    }

    // 전위 순회
    private void traversePreorder(AVLNode<T, E> node, List<T> keys) {
        if (node != null) {
            keys.add(node.key);
            traversePreorder(node.left, keys);
            traversePreorder(node.right, keys);
        }
    }
}
