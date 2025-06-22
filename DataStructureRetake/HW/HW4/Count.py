from collections import defaultdict

def build_undirected_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # 양방향 추가
    return graph

def count_simple_paths(graph, start, end):
    def dfs(node, visited, path):
        if node == end:
            print("->".join(path))  # 경로 출력
            return 1
        count = 0
        for nxt in graph[node]:
            if nxt not in visited:
                count += dfs(nxt, visited | {nxt}, path + [nxt])
        return count
    return dfs(start, {start}, [start])

def find_all_simple_cycles(graph):
    # 모든 사이클을 set에 저장 (순서 상관없이 중복제거)
    cycles = set()
    def dfs(start, current, visited, path):
        for nxt in graph[current]:
            if nxt == start and len(path) >= 2:
                cycle = tuple(sorted(path))
                cycles.add(cycle)
            elif nxt not in visited:
                dfs(start, nxt, visited | {nxt}, path + [nxt])
    nodes = list(graph.keys())
    for node in nodes:
        dfs(node, node, {node}, [node])
    # 순서/회전/반전 중복 제거
    final_cycles = set()
    for cyc in cycles:
        if len(cyc) >= 3:  # 사이클은 3개 이상 정점
            cyc_sorted = tuple(sorted(cyc))
            final_cycles.add(cyc_sorted)
    return len(final_cycles)

"""
def find_all_simple_cycles(graph):
    cycles = set()
    def dfs(start, current, visited, path):
        for nxt in graph[current]:
            if nxt == start and len(path) >= 3:
                # 순서가 중요하니 tuple(path+[start])로 저장
                cycles.add(tuple(path + [start]))
            elif nxt not in visited:
                dfs(start, nxt, visited | {nxt}, path + [nxt])
    nodes = list(graph.keys())
    for node in nodes:
        dfs(node, node, {node}, [node])
    return len(cycles)
"""

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f if line.strip()]
    start, end = lines[0].split()
    edges = [tuple(line.split()) for line in lines[1:]]

    graph = build_undirected_graph(edges)
    path_cnt = 0
    for node1 in graph:
        for node2 in graph:
            path_cnt += count_simple_paths(graph, node1, node2)
    cycle_cnt = find_all_simple_cycles(graph)
    print("simple path:", path_cnt)
    print("simple cycle:", cycle_cnt)
