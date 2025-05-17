def test(index, num, ans, lines, M):
        #print("index",index,'num',num,'ans',ans)
        if index == len(lines):
            #print("M")
            return 0,0

        elif num == 0:
            if lines[index][0] <= 0 and lines[index][1] >= M:
                ans.append(lines[index])
                #print(ans,0)
                return num+1,ans

            Max = [-1,-1]
            for i in range(index,len(lines)):
                #print(i,Max)
                if lines[i][0] <= 0 and lines[i][1] < M:
                    if Max[1] < lines[i][1]:
                        Max = [i,lines[i][1]]

            if Max[0] != -1:
                ans.append(lines[Max[0]])
                #print(ans,1)
                return test(Max[0]+1,num+1,ans,lines,M)

            else:
                #print(ans,-1)
                return 0,0
        
        else:
            if lines[index][0] <= ans[num-1][1] and lines[index][1] >= M:
                ans.append(lines[index])
                #print(ans,2)
                return num+1,ans

            Max = [-1,-1]
            for i in range(index,len(lines)):
                #print(i,Max)
                if lines[i][0] <= ans[num-1][1] and ans[num-1][1]<=lines[i][1] < M:
                    if Max[1] < lines[i][1]:
                        Max = [i,lines[i][1]]
            
            
            if Max[0] != -1:
                ans.append(lines[Max[0]])
                #print(ans,3)
                return test(Max[0]+1,num+1,ans,lines,M)
            
            else:
                #print(ans,-1)
                return 0,0

turn = int(input())

t = False

for _ in range(turn):
    a = input()
    M = int(input())
    
    lines = []
    while True:
        try:
            a, b = map(int, input().split())
        except EOFError:
            break
        if a == 0 and b == 0:
            break
        if b > 0:
            lines.append([a,b])

    lines.sort()
    
    num, ans = test(0,0,[],lines,M)

    if t:
        print()

    t = True


    print(num)

    if num > 0:
        for i in ans:
            print(i[0],i[1])

