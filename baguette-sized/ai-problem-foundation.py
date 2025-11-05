import heapq

class Puzzle:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.goal = goal
        self.moves = moves
        self.zero = board.index(0)  # position of empty tile

    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

    def heuristic(self):
        # Manhattan distance: sum of distances of each tile from its goal position
        distance = 0
        for i, val in enumerate(self.board):
            if val == 0: 
                continue
            goal_i = self.goal.index(val)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_i, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
        return distance

    def is_goal(self):
        return self.board == self.goal

    def get_neighbors(self):
        neighbors = []
        x, y = divmod(self.zero, 3)
        moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_zero = nx*3 + ny
                new_board = self.board[:]
                new_board[self.zero], new_board[new_zero] = new_board[new_zero], new_board[self.zero]
                neighbors.append(Puzzle(new_board, self.goal, self.moves + 1))
        return neighbors

def a_star(start):
    open_set = []
    heapq.heappush(open_set, (start.heuristic(), start))
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if tuple(current.board) in visited:
            continue
        visited.add(tuple(current.board))

        if current.is_goal():
            return current.moves

        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(open_set, (neighbor.moves + neighbor.heuristic(), neighbor))

    return -1  # No solution

# Example usage
start = Puzzle([1, 2, 3,
                4, 0, 6,
                7, 5, 8],
               goal=[1, 2, 3,
                     4, 5, 6,
                     7, 8, 0])

steps = a_star(start)
print(f"Solution found in {steps} moves.")
