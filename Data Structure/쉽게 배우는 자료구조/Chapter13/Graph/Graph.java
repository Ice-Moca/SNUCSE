import list.LinkedList;
import java.util.*;

/* Graph 클래스

vertices: 노드 개수
adjList: 인접 리스트로 그래프를 표현
addEdge(): 간선 추가 메서드

//////////////////////////
BFS (너비 우선 탐색)

Queue를 사용하여 탐색 진행
visited 배열로 방문 여부 체크

//////////////////////////
DFS (깊이 우선 탐색)

재귀 호출을 사용하여 구현
visited 배열을 사용하여 방문한 노드를 추적
*/

class Graph {
    private int vertices;
    private LinkedList<Integer>[] adjList;

    public Graph(int vertices) {
        this.vertices = vertices;
        adjList = new LinkedList[vertices];
        for (int i = 0; i < vertices; i++) {
            adjList[i] = new LinkedList<>();
        }
    }

    public void addEdge(int src, int dest) {
        adjList[src].append(dest);
        adjList[dest].append(src); // 무방향 그래프
    }

    public void bfs(int start) {
        boolean[] visited = new boolean[vertices];
        Queue<Integer> queue = new LinkedList<>();
        visited[start] = true;
        queue.add(start);

        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");
            
            for (int i = 0; i < adjList[node].len(); i++) {
                int neighbor = adjList[node].get(i);
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
        System.out.println();
    }

    public void dfs(int start) {
        boolean[] visited = new boolean[vertices];
        dfsRecursive(start, visited);
        System.out.println();
    }

    private void dfsRecursive(int node, boolean[] visited) {
        visited[node] = true;
        System.out.print(node + " ");
        
        for (int i = 0; i < adjList[node].len(); i++) {
            int neighbor = adjList[node].get(i);
            if (!visited[neighbor]) {
                dfsRecursive(neighbor, visited);
            }
        }
    }

    public static void main(String[] args) {
        Graph graph = new Graph(6);
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 4);
        graph.addEdge(3, 5);
        graph.addEdge(4, 5);

        System.out.println("BFS Traversal: ");
        graph.bfs(0);
        
        System.out.println("DFS Traversal: ");
        graph.dfs(0);
    }
}
