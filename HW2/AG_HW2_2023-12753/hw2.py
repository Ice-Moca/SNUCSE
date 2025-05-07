import sys
import time

def build_adjacency_matrix(vertex_count, edge_list):
    # Make the adjacency matrix
    # Initialize matix with False values
    adjacency_matrix = []
    for _ in range(vertex_count):
        adjacency_matrix.append([False] * vertex_count)
    # Fill the adjacency matrix with edges
    for source, target in edge_list:
        adjacency_matrix[source][target] = True

    # Make transposed adjacency matrix
    # Initialize matix with False values
    transpose_matrix = []
    for _ in range(vertex_count):
        transpose_matrix.append([False] * vertex_count)
    # Fill the transposed adjacency matrix with edges
    for source, target in edge_list:
        transpose_matrix[target][source] = True

    return adjacency_matrix, transpose_matrix

# reference: https://velog.io/@yeseolee/python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8Linked-List-feat.LeetCode
class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def build_adjacency_list(vertex_count, edge_list):
    # Initialize head pointers for each vertex
    adjacency_heads = [None] * vertex_count
    transpose_heads = [None] * vertex_count

    # Insert each edge at the head for O(1) insertion
    for source, target in edge_list:
        # forward edge
        node = ListNode(target, adjacency_heads[source])
        adjacency_heads[source] = node
        # transpose edge
        tnode = ListNode(source, transpose_heads[target])
        transpose_heads[target] = tnode

    return adjacency_heads, transpose_heads

def build_adjacency_array(vertex_count, edge_list):
    # Get the number of edges
    total_edges = len(edge_list)

    # Compute degree for each vertex
    degree_count = [0] * vertex_count
    for source, _ in edge_list:
        degree_count[source] += 1

    # Compute prefix sums to determine end positions of vertices
    prefix_degree = [0] * (vertex_count + 1)
    for index in range(1, vertex_count + 1):
        prefix_degree[index] = prefix_degree[index - 1] + degree_count[index - 1]
        
    # Get the start position in array of each vertices
    index = prefix_degree[:-1].copy()

    # Fill adjacency arrays
    adjacency_array = [0] * total_edges
    for source, target in edge_list:
        adjacency_array[index[source]] = target
        index[source] += 1

    # Compute in-degree for transpose
    in_degree_count = [0] * vertex_count
    for _, target in edge_list:
        in_degree_count[target] += 1

    # Compute prefix sums for transpose
    transpose_prefix = [0] * (vertex_count + 1)
    for index in range(1, vertex_count + 1):
        transpose_prefix[index] = transpose_prefix[index - 1] + in_degree_count[index - 1]

    # Get the start position in array of each vertices for transpose
    index_transpose = transpose_prefix[:-1].copy()
    
    # Fill transpose arrays
    transpose_adjacency_array = [0] * total_edges
    for source, target in edge_list:
        transpose_adjacency_array[index_transpose[target]] = source
        index_transpose[target] += 1

    return (prefix_degree, adjacency_array), (transpose_prefix, transpose_adjacency_array)

# Kosaraju's algorithm to find strongly connected components in a directed graph
# reference: https://wondy1128.tistory.com/130

def depth_first_search_order(source_vertex, visited_nodes, finish_stack, graph_structure, representation_mode, vertex_count):
    """
    First DFS pass: marks visited nodes and pushes onto finish_stack in order of completion.
    """
    # Mark the current node as visited
    visited_nodes[source_vertex] = True
    # Check the representation mode
    if representation_mode == 'matrix':
        adjacency_matrix = graph_structure
        # Check all vertices to find neighbors
        for neighbor in range(vertex_count):
            # Check if there is an edge and if neighbor is not visited
            if adjacency_matrix[source_vertex][neighbor] and not visited_nodes[neighbor]:
                # Recursively visit the neighbor until all neighbors are visited
                depth_first_search_order(neighbor, visited_nodes, finish_stack, graph_structure, representation_mode, vertex_count)
    if representation_mode == 'list':
        adjacency_heads = graph_structure
        node = adjacency_heads[source_vertex]
        # Check all vertices to find neighbors
        while node:
            if not visited_nodes[node.val]:
                # Check if there is an edge and if neighbor is not visited
                depth_first_search_order(node.val, visited_nodes, finish_stack, graph_structure, representation_mode, vertex_count)
            node = node.next
    if representation_mode == 'array':
        # as we give the output of adjacency_array as a tuple, we need to unpack it
        # use pointer_array to check the index of start and end of the vertex
        pointer_array, adjacency_array = graph_structure
        # Check all neighbors in the adjacency array
        for index in range(pointer_array[source_vertex], pointer_array[source_vertex + 1]):
            neighbor = adjacency_array[index]
            # check if neighbor is not visited
            if not visited_nodes[neighbor]:
                # Recursively visit the neighbor until all neighbors are visited
                depth_first_search_order(neighbor, visited_nodes, finish_stack, graph_structure, representation_mode, vertex_count)
    # Push the current node onto the stack
    finish_stack.append(source_vertex)


def depth_first_search_collect(source_vertex, visited_nodes, component_vertices, transpose_structure, representation_mode, vertex_count):
    """
    Second DFS pass on transposed graph: collects strongly connected component vertices.
    """
    # Mark the current node as visited
    visited_nodes[source_vertex] = True
    # Add the current node to the component vertices
    component_vertices.append(source_vertex)
    # Check the representation mode
    if representation_mode == 'matrix':
        transpose_matrix = transpose_structure
        # Check all vertices to find neighbors
        for neighbor in range(vertex_count):
            # Check if there is an edge and if neighbor is not visited
            if transpose_matrix[source_vertex][neighbor] and not visited_nodes[neighbor]:
                # Recursively visit the neighbor until all neighbors are visited
                depth_first_search_collect(neighbor, visited_nodes, component_vertices, transpose_structure, representation_mode, vertex_count)
    if representation_mode == 'list':
        transpose_heads = transpose_structure
        node = transpose_heads[source_vertex]
        # Check all vertices to find neighbors
        while node:
            if not visited_nodes[node.val]:
                # Recursively visit the neighbor until all neighbors are visited
                depth_first_search_collect(node.val, visited_nodes, component_vertices, transpose_structure, representation_mode, vertex_count)
            node = node.next
    if representation_mode == 'array':  
        # as we give the output of adjacency_array as a tuple, we need to unpack it
        transpose_pointer, transpose_array = transpose_structure
        for index in range(transpose_pointer[source_vertex], transpose_pointer[source_vertex + 1]):
            neighbor = transpose_array[index]
            if not visited_nodes[neighbor]:
                # Recursively visit the neighbor until all neighbors are visited
                depth_first_search_collect(neighbor, visited_nodes, component_vertices, transpose_structure, representation_mode, vertex_count)


def kosaraju_strongly_connected_components(vertex_count, graph_structure, transpose_structure, representation_mode):
    """
    Kosaraju's algorithm to find strongly connected components in a directed graph.
    """
    sys.setrecursionlimit(max(1000000, vertex_count + 10))
    visited_nodes = [False] * vertex_count
    finish_stack = []

    # 1) First DFS pass to compute finish stack
    # finish_stack: list of vertices in the order 
    for node in range(vertex_count):
        if not visited_nodes[node]:
            depth_first_search_order(node, visited_nodes, finish_stack, graph_structure, representation_mode, vertex_count)

    # 2) Reset visited markers for second pass
    visited_nodes = [False] * vertex_count
    strongly_connected_components = []

    # 3) Second DFS pass on transposed graph to collect components
    while finish_stack:
        # Pop a vertex from the finish stack
        node = finish_stack.pop()
        if not visited_nodes[node]:
            component_vertices = []
            # Collect strongly connected component vertices
            # component_vertices: list of vertices in the current strongly connected component
            # visited_nodes are updated through the recursive process of depth_first_search_collect
            # So we can get the group of strongly connected components 
            depth_first_search_collect(node, visited_nodes, component_vertices, transpose_structure, representation_mode, vertex_count)
            strongly_connected_components.append(component_vertices)

    return strongly_connected_components


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['-m', '-l', '-a']:
        print("Usage: python3 hw2.py [-m|-l|-a] < input.txt > output.txt", file=sys.stderr)
        sys.exit(1)
    representation_option = sys.argv[1]

    # Read input
    input_data = sys.stdin.read().split()
    # Read the number of vertices and edges
    vertex_count, edge_count = map(int, input_data[:2])
    # Read the edges from the input
    edge_tokens = iter(input_data[2:])
    # Create a list of edges as tuples (source, target)
    edge_list = []
    for source, target in zip(edge_tokens, edge_tokens):
        source = int(source)
        target = int(target)
        edge_list.append((source, target))

    # Check the representation mode
    # Then make the adjacency matrix, list or array
    if representation_option == '-m':
        graph_structure, transpose_structure = build_adjacency_matrix(vertex_count, edge_list)
        representation_mode = 'matrix'
    if representation_option == '-l':
        graph_structure, transpose_structure = build_adjacency_list(vertex_count, edge_list)
        representation_mode = 'list'
    if representation_option == '-a':
        graph_structure, transpose_structure = build_adjacency_array(vertex_count, edge_list)
        representation_mode = 'array'

    # Check the execution time
    start_time = time.perf_counter()
    scc_results = kosaraju_strongly_connected_components(vertex_count, graph_structure, transpose_structure, representation_mode)
    end_time = time.perf_counter()

    # Sort the strongly connected components in lexicographical order
    # and print the result
    for component in scc_results:
        component.sort()
    scc_results.sort()
    for component in scc_results:
        print(" ".join(map(str, component)))
    # Print the execution time in milliseconds
    elapsed_ms = (end_time - start_time) * 1000
    print(f"{elapsed_ms:.6f}")

if __name__ == "__main__":
    main()
