n, k = map(int,input().split())
a = list(map(int,input().split()))

s = 1

for i in a:
    s = s*i
    if len(str(s))>k:
        s = 1

print(s)