import list.LinkedList;
import java.util.*;

//무향 그래프에서 알고리즘
//프림, 다익스트라, 크루샬 알고리즘
//유향 그래프일 경우 다른 알고리즘이 필요하다.

class GraphAlgor {
    private int vertices;
    private LinkedList<Integer>[] adjList;
    private int[][] weightMatrix;

    public GraphAlgor(int vertices) {
        this.vertices = vertices;
        adjList = new LinkedList[vertices];
        weightMatrix = new int[vertices][vertices];
        for (int i = 0; i < vertices; i++) {
            adjList[i] = new LinkedList<>();
        }
    }

    public void addEdge(int src, int dest, int weight) {
        adjList[src].append(dest);
        adjList[dest].append(src); // 무향 그래프
        weightMatrix[src][dest] = weight;
        weightMatrix[dest][src] = weight;
    }

    public void primMST() {
        boolean[] inMST = new boolean[vertices];
        int[] key = new int[vertices];
        int[] parent = new int[vertices];
        Arrays.fill(key, Integer.MAX_VALUE);
        key[0] = 0;
        parent[0] = -1;

        for (int count = 0; count < vertices - 1; count++) {
            int u = -1;
            for (int v = 0; v < vertices; v++) {
                if (!inMST[v] && (u == -1 || key[v] < key[u])) {
                    u = v;
                }
            }
            inMST[u] = true;
            for (int v = 0; v < vertices; v++) {
                if (weightMatrix[u][v] != 0 && !inMST[v] && weightMatrix[u][v] < key[v]) {
                    parent[v] = u;
                    key[v] = weightMatrix[u][v];
                }
            }
        }

        System.out.println("Prim's MST:");
        for (int i = 1; i < vertices; i++) {
            System.out.println(parent[i] + " - " + i + " (Weight: " + weightMatrix[i][parent[i]] + ")");
        }
    }

    public void dijkstra(int start) {
        int[] dist = new int[vertices];
        boolean[] visited = new boolean[vertices];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        for (int i = 0; i < vertices - 1; i++) {
            int u = -1;
            for (int j = 0; j < vertices; j++) {
                if (!visited[j] && (u == -1 || dist[j] < dist[u])) {
                    u = j;
                }
            }
            visited[u] = true;

            for (int v = 0; v < vertices; v++) {
                if (!visited[v] && weightMatrix[u][v] != 0 && dist[u] + weightMatrix[u][v] < dist[v]) {
                    dist[v] = dist[u] + weightMatrix[u][v];
                }
            }
        }
        System.out.println("Dijkstra's Shortest Paths:");
        for (int i = 0; i < vertices; i++) {
            System.out.println("Node " + i + " Distance: " + dist[i]);
        }
    }

    class Edge implements Comparable<Edge> {
        int src, dest, weight;
        public Edge(int src, int dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }
        public int compareTo(Edge other) {
            return this.weight - other.weight;
        }
    }

    public void kruskalMST() {
        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            for (int j = i + 1; j < vertices; j++) {
                if (weightMatrix[i][j] != 0) {
                    edges.add(new Edge(i, j, weightMatrix[i][j]));
                }
            }
        }
        Collections.sort(edges);
        int[] parent = new int[vertices];
        for (int i = 0; i < vertices; i++) {parent[i] = i;}

        System.out.println("Kruskal's MST:");
        for (Edge edge : edges) {
            if (find(edge.src) != find(edge.dest)) {
                System.out.println(edge.src + " - " + edge.dest + " (Weight: " + edge.weight + ")");
                union(edge.src, edge.dest);
            }
        }
    }

    public int find(int v) {
        if (parent[v] != v) parent[v] = find(parent[v]);
        return parent[v];
    }

    public void union(int u, int v) {
        parent[find(u)] = find(v);
    }

    public static void main(String[] args) {
        GraphAlgor graph = new GraphAlgor(6);
        graph.addEdge(0, 1, 4);
        graph.addEdge(0, 2, 4);
        graph.addEdge(1, 2, 2);
        graph.addEdge(1, 3, 5);
        graph.addEdge(2, 3, 8);
        graph.addEdge(2, 4, 10);
        graph.addEdge(3, 4, 2);
        graph.addEdge(3, 5, 6);
        graph.addEdge(4, 5, 3);

        System.out.println("Prim's Algorithm:");
        graph.primMST();
        
        System.out.println("\nDijkstra's Algorithm (starting from node 0):");
        graph.dijkstra(0);
        
        System.out.println("\nKruskal's Algorithm:");
        graph.kruskalMST();
    }
}
