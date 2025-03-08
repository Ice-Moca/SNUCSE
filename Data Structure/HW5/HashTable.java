import java.util.*;

public class HashTable<K extends Comparable<K>, V> {
    static final int TABLE_SIZE = 100;

    private final AVLTree<K, V>[] slots;

    public HashTable() {
        slots = new AVLTree[TABLE_SIZE];
        for (int i = 0; i < TABLE_SIZE; i++) {
            slots[i] = new AVLTree<>();
        }
    }

    private int computeHash(K key) {
        if (key instanceof String) {
            return ((String) key).chars().sum() % TABLE_SIZE;
        }
        return Math.abs(key.hashCode()) % TABLE_SIZE;
    }

    public void add(K key, V value) {
        int index = computeHash(key);
        slots[index].add(key, value);
    }

    public List<K> getKeysAtSlot(int index) {
        return slots[index].getPreorderKeys();
    }

    public List<V> findValues(K key) {
        int index = computeHash(key);
        return slots[index].findValues(key);
    }
}
