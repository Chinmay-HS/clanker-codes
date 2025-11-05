import heapq

class Node:
    def __init__(self, name, pos):
        self.name, self.pos = name, pos
        self.g = self.h = self.f = float('inf')
        self.parent = None
    def __lt__(self, o): return self.f < o.f
    def __hash__(self): return hash(self.name)
    def __eq__(self, o): return self.name == o.name

def heuristic(a, b): return abs(a.pos[0]-b.pos[0]) + abs(a.pos[1]-b.pos[1])
def distance(a, b): return 1
def path(n):
    p = []
    while n: p.insert(0, n.name); n = n.parent
    return p

def A_star(start, goal, graph):
    open, closed = [], set()
    start.g, start.h, start.f = 0, heuristic(start, goal), heuristic(start, goal)
    heapq.heappush(open, start)
    while open:
        cur = heapq.heappop(open)
        if cur == goal: return path(cur)
        closed.add(cur)
        for nb in graph[cur]:
            if nb in closed: continue
            g = cur.g + distance(cur, nb)
            if g < nb.g:
                nb.parent, nb.g = cur, g
                nb.h, nb.f = heuristic(nb, goal), g + heuristic(nb, goal)
                if nb not in open: heapq.heappush(open, nb)
    return None

# ---------- Example ----------
A, B, C, D, E = Node('A',(0,0)), Node('B',(1,0)), Node('C',(1,1)), Node('D',(0,1)), Node('E',(2,1))
graph = {A:[B,D], B:[A,C], C:[B,D,E], D:[A,C], E:[C]}
print("Path found:", " → ".join(A_star(A, E, graph)))
