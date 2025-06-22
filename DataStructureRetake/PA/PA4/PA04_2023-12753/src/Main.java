import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        HashTable ht = new HashTable();
        String line;

        while ((line = reader.readLine()) != null) {
            line = line.strip();
            if (line.isEmpty()) {
                continue;
            }
            String[] parts = line.split("\\s+");
            String cmd = parts[0];

            switch (cmd) {
                case "create":
                    int c1 = Integer.parseInt(parts[1]);
                    int c2 = Integer.parseInt(parts[2]);
                    int c3 = Integer.parseInt(parts[3]);
                    ht.create(c1, c2, c3);
                    break;

                case "insert":
                    int keyToInsert = Integer.parseInt(parts[1]);
                    ht.insert(keyToInsert);
                    break;

                case "delete":
                    int keyToDelete = Integer.parseInt(parts[1]);
                    ht.delete(keyToDelete);
                    break;

                case "search":
                    int keyToSearch = Integer.parseInt(parts[1]);
                    ht.search(keyToSearch);
                    break;

                case "rehash":
                    ht.rehash();
                    break;

                case "cleanup":
                    ht.cleanup();
                    break;

                case "quit":
                    return;

                default:
                    throw new IllegalArgumentException("Unknown command: " + cmd);
            }
        }
    }
}