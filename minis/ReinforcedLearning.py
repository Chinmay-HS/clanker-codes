import random
grid=['S','.','P','.','P','.','.','.','G']
Q={}
def move(p,a):
    if a==0 and p%3>0:return p-1
    if a==1 and p%3<2:return p+1
    if a==2 and p>=3:return p-3
    if a==3 and p<6:return p+3
    return p
for _ in range(200):
    p=0
    for __ in range(10):
        a=random.randint(0,3) if random.random()<0.3 else max(range(4),key=lambda x:Q.get((p,x),0))
        n=move(p,a)
        r=100 if grid[n]=='G' else -100 if grid[n]=='P' else -1
        o=Q.get((p,a),0)
        Q[(p,a)]=o+0.1*(r+0.9*max([Q.get((n,i),0) for i in range(4)])-o)
        p=n
        if grid[p]in['G','P']:break
p,pa=0,[0]
for _ in range(10):
    a=max(range(4),key=lambda x:Q.get((p,x),0))
    p=move(p,a)
    pa.append(p)
    if grid[p]in['G','P']:break
print("Path:",' → '.join(map(str,pa)))
print("Result:","Goal!"if grid[p]=='G'else"Pit!")
