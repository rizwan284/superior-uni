# Code of A* Algorithm (without importing any library)

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class AStar:
    def __init__(self, start, end, grid):
        self.start = Node(None, start)
        self.end = Node(None, end)
        self.grid = grid
        self.open_list = []
        self.closed_list = []

    def heuristic(self, node):
        return abs(node.position[0] - self.end.position[0]) + abs(node.position[1] - self.end.position[1])

    def get_neighbors(self, node):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        for direction in directions:
            neighbor = (node.position[0] + direction[0], node.position[1] + direction[1])
            if 0 <= neighbor[0] < len(self.grid) and 0 <= neighbor[1] < len(self.grid[0]) and self.grid[neighbor[0]][neighbor[1]] == 0:
                neighbors.append(Node(node, neighbor))
        return neighbors

    def find_path(self):
        self.open_list.append(self.start)
        while self.open_list:
            current_node = min(self.open_list, key=lambda node: node.f)
            self.open_list.remove(current_node)
            self.closed_list.append(current_node)

            if current_node == self.end:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]

            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor in self.closed_list:
                    continue

                neighbor.g = current_node.g + 1
                neighbor.h = self.heuristic(neighbor)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor in self.open_list:
                    existing_node = self.open_list[self.open_list.index(neighbor)]
                    if neighbor.g < existing_node.g:
                        existing_node.g = neighbor.g
                        existing_node.f = neighbor.f
                        existing_node.parent = current_node
                else:
                    self.open_list.append(neighbor)
        return None

def main():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0]
    ]
    start = (0, 1)  
    end = (4, 4)    
    astar = AStar(start, end, grid)
    path = astar.find_path()
    print("Path:", path)

if __name__ == "__main__":
    main()