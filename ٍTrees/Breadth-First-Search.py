graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

def bfs(graph, node):
    queue = []
    visited = []

    queue.append(node)
    visited.append(node)



    while queue:

        s = queue.pop(0)

        print(s, end=" ")

        for node in graph[s]:
            if node not in visited:
                queue.append(node)
                visited.append(node)



bfs(graph, 'A')
