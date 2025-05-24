h, w, n = map(int,input().split())

Map = [[0]*w for _ in range(h)]


for _ in range(n):
    x, y = map(int,input().split())
    Map[x-1][y-1] = 1

q = int(input())

for _ in range(q):
    t, x = map(int,input().split())
    count = 0
    if t == 2:
        for i in Map:
            if i[x-1] == 1:
                i[x-1] = 0
                count +=1
    elif t == 1:
        count = sum(Map[x-1])
        Map[x-1] = [0]*w

    print(count)