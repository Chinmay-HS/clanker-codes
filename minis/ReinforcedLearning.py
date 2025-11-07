import random
Q=[0,0,0,0,0]           # 5 states in a line
for _ in range(500):     # train 500 episodes
    s=0
    while s<4:
        a=random.choice([-1,1])            
        ns=max(0,min(4,s+a))
        r=10 if ns==4 else -1
        Q[s]+=0.1*(r+0.9*Q[ns]-Q[s])      
        s=ns
print("Learned Q-values:",Q)
