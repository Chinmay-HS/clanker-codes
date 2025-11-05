import numpy as np

def f(x): return -x[0]**2 + 5
def neighbors(x, s=0.1): return [x + s, x - s]

def hill_climb(f, x0, steps=100, s=0.1):
    x, fx = np.array([x0]), f(np.array([x0]))
    for i in range(steps):
        n = neighbors(x, s)
        nv = [f(y) for y in n]
        best = np.argmax(nv)
        if nv[best] > fx:
            x, fx = n[best], nv[best]
            print(f"Step {i+1}: x={x[0]:.3f}, f(x)={fx:.3f}")
        else:
            print("Converged."); break
    return x, fx

x, val = hill_climb(f, 2.0, 100, 0.1)
print(f"\nBest: x={x[0]:.3f}, f(x)={val:.3f}")
