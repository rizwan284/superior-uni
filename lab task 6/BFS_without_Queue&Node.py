# BFS without Queue & without Node

def bfs(tree, start):
    visited = []

    def bfs_traversal(node):
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            for neighbor in tree[node]:
                bfs_traversal(neighbor)

    bfs_traversal(start)

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