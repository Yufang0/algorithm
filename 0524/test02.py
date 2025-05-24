n, q = map(int,input().split())

Q = []

for _ in range(q):
    t, u, v = map(int,input().split())

    if t == 0:
        Q.append([u,v])
        Q.append([v,u])
    elif t == 1:
        if [u,v] in Q:
            print(1)
            
        else:
            print(0)