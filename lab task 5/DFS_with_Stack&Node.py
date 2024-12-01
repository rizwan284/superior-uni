#  DFS with Stack & Node

tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}

def dfs_stack(start, goal):
    stack = [start]  
    visited = []  

    while stack:
        node = stack.pop() 
        if node not in visited:
            visited.append(node)  
            if node == goal:
                return visited  
            
            stack.extend(reversed(tree[node]))

    return visited

visited_nodes = dfs_stack('A', 'F')
print(visited_nodes)





