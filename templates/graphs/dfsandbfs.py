from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')  # Print the visited node
            visited.add(node)
            stack.extend(reversed(graph[node]))
    assert(len(visited) == len(graph))
    print("Done")

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')  # Print the visited node
            visited.add(node)
            queue.extend(graph[node])
    assert(len(visited) == len(graph))
    print("Done")

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

for search in [bfs, dfs]:
    search(graph, 'A')
