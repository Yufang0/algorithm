h, w, n = map(int,input().split())

rows = [0]*h
columns = [0]*w


for _ in range(n):
    x, y = map(int,input().split())
    rows[x-1] += 1
    columns[y-1] += 1

q = int(input())

for _ in range(q):
    t, g = map(int,input().split())

    if t == 2:
        print(columns[g-1])
        columns[g-1] = 0

    elif t == 1:
        print(rows[g-1])