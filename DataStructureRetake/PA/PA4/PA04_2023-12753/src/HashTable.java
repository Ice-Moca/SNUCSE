public class HashTable {
    private int[] table;
    private int c1, c2, c3, size;

    private void resetTable(int newSize) {
        table = new int[newSize];
        for (int i = 0; i < newSize; i++) {
            table[i] = 0;
        }
    }

    public void create(int c1, int c2, int c3) {
        this.c1 = c1;
        this.c2 = c2;
        this.c3 = c3;
        this.size = 127;
        resetTable(this.size);
    }

    public void create(int c1, int c2, int c3, int newSize) {
        this.c1 = c1;
        this.c2 = c2;
        this.c3 = c3;
        this.size = newSize;
        resetTable(this.size);
    }

    public void insert(int key) {
        internalInsert(key, false);
        rehashCheck();
    }

    private int findIndex(int key, boolean isSearch) {
        int origin = key % size;
        for (int attempt = 0; attempt < size; attempt++) {
            int offset = c1 * attempt * attempt + c2 * attempt + c3;
            int pos = Math.floorMod(origin + offset, size);
            int val = table[pos];

            if (isSearch) {
                if (val == 0) return -1;
                if (val == key) return pos;
            } else {
                if (val == 0 || val == -1) return pos;
            }
        }
        return -1;
    }

    private boolean internalInsert(int key, boolean silent) {
        int slot = findIndex(key, false);
        table[slot] = key;
        if (!silent) {
            System.out.println("INSERT: " + key + ", INDEX: " + slot);
        }
        return true;
    }

    public void delete(int key) {
        int location = findIndex(key, true);
        if (location == -1) {
            System.out.println("Failed to find " + key);
            return;
        }
        table[location] = -1;
        System.out.println("DELETE: " + key + ", INDEX: " + location);
        cleanupCheck();
    }

    public void search(int key) {
        int pos = findIndex(key, true);
        if (pos == -1) {
            System.out.println("Failed to find " + key);
        }
        else {
            System.out.println("SEARCH: " + key + ", INDEX: " + pos);
        }
    }

    public void rehash() {
        int[] oldTable = table;
        int oldSize = size;
        int updatedSize = nextPrimeNum(2 * size);
        create(c1, c2, c3, updatedSize);

        for (int i = 0; i < oldSize; i++){
            if (oldTable[i] > 0) internalInsert(oldTable[i], true);
        }
        System.out.println("Rehashed to " + updatedSize);
    }

    public void cleanup() {
        int[] oldTable = table;
        resetTable(size);

        for (int key : oldTable) {
            if (key > 0) internalInsert(key, true);
        }
        System.out.println("Cleanup Done");
    }

    private void rehashCheck() {
        int cnt = 0;
        for (int val : table){
            if (val > 0) cnt++;
        }
        if ((double) cnt / size >= 0.7) rehash();
    }

    private void cleanupCheck() {
        int tCount = 0;
        for (int val : table){
            if (val == -1) tCount++;
        }
        if ((double) tCount / size >= 0.2) cleanup();
    }

    private int nextPrimeNum(int start) {
        int candidate = (start % 2 == 0) ? start + 1 : start;
        while (!isPrimeNum(candidate)){
            candidate += 2;
        }
        return candidate;
    }

    private boolean isPrimeNum(int num) {
        if (num < 2) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        for (int i = 3; i * i <= num; i += 2)
            if (num % i == 0) return false;
        return true;
    }
}
