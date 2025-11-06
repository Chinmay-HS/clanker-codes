graph={'A':['B','C'],'B':['A','C'],'C':['A','B','D'],'D':['C']}
result={}
def is_safe(r,c):
    for n in graph[r]:
        if result.get(n)==c:return False
    return True
def solve(R):
    if not R:return True
    r=R[0]
    for c in['Red','Green','Blue']:
        if is_safe(r,c):
            result[r]=c
            if solve(R[1:]):return True
            del result[r]
    return False
solve(list(graph.keys()))
for r,c in result.items():print(f"{r} → {c}")
