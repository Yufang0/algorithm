L = []
H = []
R = []

while True:
    try:
        l, h, r = map(int,input().split())
    except EOFError:
        break
    
    L.append(l)
    H.append(h)
    R.append(r)

ans = [L[0],H[0]]
index = [0]
hlist = [H[0]]
Max = [0,0]


for i in range(1,max(R)+1):
    
    for j in range(len(L)):
        print("a",i,j,index)

        if L[j] == i:
            hlist.append(H[j])
            index.append(j)
        else:
            break

    for j in index:
        print("b",i,j,index)
        if R[j] > i:
            hlist.remove(H[j])
            index.remove(j)
        if Max[1] < H[j]:
            Max[0] = j
            Max[1] = H[j]
    print(ans[len(ans)-1], Max[1])
    if ans[len(ans)-1] < Max[1]:
        
        ans.append(L[Max[0]])
        ans.append(Max[1]) 

print(" ".join(map(str, ans)))
        

