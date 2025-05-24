n = int(input())

p = list(map(int,input().split()))

ans = []
count = 0

for i in range(1,n-1):
    if p[i-1] < p[i] > p[i+1]: 
        ans.append([1,i-1,i+1])
    elif p[i-1] > p[i] < p[i+1]:
        ans.append([-1,i-1,i+1])

for i in range(len(ans)-1):
    if ans[i][0] == 1 and ans[i+1][0] == -1: 
        #print("a")  
        count += 1
        if i > 0:
            for j in range(ans[i][1]-1,ans[i-1][1],-1):
                if p[j] < p[j+1]:
                    count += 1
                    #print("b","i:",i,"j:",j)

        if i < (len(ans)-1):
            count += (ans[i+2][2]-1)-ans[i+1][2]

print(count)
