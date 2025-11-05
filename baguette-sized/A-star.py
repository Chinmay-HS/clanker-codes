import heapq

class Node:
    def __init__(self, name, position):
        self.name = name                # Label
        self.position = position        # (x, y) coordinate
        self.g = float('inf')           # Cost from start
        self.h = 0                      # Heuristic cost
        self.f = float('inf')           # Total cost
        self.parent = None              # For path reconstruction

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

def heuristic(a, b):
    """Manhattan distance heuristic."""
    return abs(a.position[0] - b.position[0]) + abs(a.position[1] - b.position[1])

def distance(a, b):
    """Uniform cost between connected nodes."""
    return 1

def reconstruct_path(current):
    """Reconstruct path from goal to start."""
    path = []
    while current:
        path.insert(0, current.name)
        current = current.parent
    return path

def A_Star(start, goal, graph):
    """A* Search algorithm."""
    open_list = []
    closed_list = set()

    start.g = 0
    start.h = heuristic(start, goal)
    start.f = start.g + start.h
    heapq.heappush(open_list, start)

    while open_list:
        current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(current)

        closed_list.add(current)

        for neighbor in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g = current.g + distance(current, neighbor)

            if tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)

    return None  # No path found


# ---------------------- USAGE EXAMPLE ----------------------

# Create nodes
A = Node('A', (0, 0))
B = Node('B', (1, 0))
C = Node('C', (1, 1))
D = Node('D', (0, 1))
E = Node('E', (2, 1))

# Define graph connections
graph = {
    A: [B, D],
    B: [A, C],
    C: [B, D, E],
    D: [A, C],
    E: [C]
}

# Run A* from A to E
path = A_Star(A, E, graph)

if path:
    print("Path found:", " → ".join(path))
else:
    print("No path found.")
