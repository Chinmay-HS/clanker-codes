import heapq

class Puzzle:
    def __init__(self, board, goal, moves=0):
        self.b, self.g, self.m = board, goal, moves

    def h(self):  # Heuristic: Manhattan distance
        return sum(abs((self.b.index(x)//3)-(self.g.index(x)//3)) +
                   abs((self.b.index(x)%3)-(self.g.index(x)%3)) for x in self.b if x)

    def neighbors(self):  # Successor function
        z = self.b.index(0)
        x, y = divmod(z, 3)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nb = self.b[:]
                nb[z], nb[nx*3+ny] = nb[nx*3+ny], nb[z]
                yield Puzzle(nb, self.g, self.m+1)

def a_star(start):  # A* Search
    open, seen = [(start.h(), start)], set()
    while open:
        _, node = heapq.heappop(open)
        if tuple(node.b) in seen: continue
        seen.add(tuple(node.b))
        if node.b == node.g: return node.m  # Goal test
        for nb in node.neighbors():
            if tuple(nb.b) not in seen:
                heapq.heappush(open, (nb.m + nb.h(), nb))
    return -1

# Initial + Goal states
start = Puzzle([1,2,3,4,0,6,7,5,8], [1,2,3,4,5,6,7,8,0])
print("Solution found in", a_star(start), "moves.")
