  # BFS with Queue & Node

def bfs(tree, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            queue.extend(tree[node])

tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}

bfs(tree, 'A')

