from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'M'],
    'M': []
}

def bfs(graph, node):
    visited = []
    stack = deque()

    stack.append(node)
    visited.append(node)

    while stack:
        s = stack.pop()

        print(s, end=" ")

        for node in reversed(graph[s]):
            if node not in visited:
                stack.append(node)
                visited.append(node)



bfs(graph, 'A')
