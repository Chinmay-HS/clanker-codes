from collections import defaultdict

class Graph:
    def __init__(self, v): self.g, self.V = defaultdict(list), v
    def add(self, u, v): self.g[u].append(v)

    def DLS(self, s, t, d):
        if s == t: return True
        if d == 0: return False
        return any(self.DLS(n, t, d-1) for n in self.g[s])

    def IDDFS(self, s, t, maxD):
        return any(self.DLS(s, t, d) for d in range(maxD+1))

# Example usage
g = Graph(7)
edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
for u,v in edges: g.add(u,v)

src, target, depth = 0, 6, 3
print("Reachable" if g.IDDFS(src, target, depth) else "Not reachable")