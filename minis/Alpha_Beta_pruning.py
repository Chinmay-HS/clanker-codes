class Node:
    def __init__(self, name, children=None, value=None):
        self.name, self.children, self.value = name, children or [], value

def alpha_beta(node, depth, alpha, beta, maximizing):
    if depth == 0 or node.value is not None:
        return node.value
    if maximizing:
        val = float('-inf')
        for c in node.children:
            val = max(val, alpha_beta(c, depth-1, alpha, beta, False))
            alpha = max(alpha, val)
            if beta <= alpha: break
        return val
    else:
        val = float('inf')
        for c in node.children:
            val = min(val, alpha_beta(c, depth-1, alpha, beta, True))
            beta = min(beta, val)
            if beta <= alpha: break
        return val

# Game tree
A = Node('A', [
    Node('B', [Node('D', value=3), Node('E', value=5), Node('F', value=6)]),
    Node('C', [Node('G', value=9), Node('H', value=1), Node('I', value=2)])
])

print("The optimal value is:", alpha_beta(A, 3, float('-inf'), float('inf'), True))
