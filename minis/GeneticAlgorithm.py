import random

def fitness(x):
    return -x**2 + 10*x + 5  # Quadratic function to maximize

population = [random.randint(0, 15) for _ in range(6)]
print("Genetic Algorithm - Maximizing -x² + 10x + 5")
print("Initial population:", population)

for generation in range(5):
    scores = [(fitness(x), x) for x in population]
    scores.sort(reverse=True)
    best_score, best_individual = scores[0]
    print(f"Generation {generation}: Best = {best_individual}, Fitness = {best_score:.2f}")
    
    # Selection and crossover
    parents = [x for _, x in scores[:3]]
    population = []
    for _ in range(6):
        p1, p2 = random.sample(parents, 2)
        child = (p1 + p2) // 2 + random.randint(-1, 1)
        child = max(0, min(15, child))  # Keep in bounds
        population.append(child)

print("Final population:", population)