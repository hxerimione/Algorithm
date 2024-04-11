import sys
input = sys.stdin.readline
n, l = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

answer = 2*n
for i in range(n):
    hor = []
    ver = []
    for j in range(n):
        hor.append(graph[i][j])
        ver.append(graph[j][i])
    acc_h = 1
    acc_v = 1
    val_h = hor[0]
    val_v = ver[0]
    check_h = False
    check_v = False
    ans_h = True
    ans_v = True
    for h in hor[1:]:
        if check_h and acc_h ==l :
            check_h = False
            acc_h = 0
        if val_h < h : # 커짐
            if h - val_h >=2 :
                ans_h = False
                break
            if check_h :
                check_h = False
                ans_h = False
                break
            if acc_h < l:#지금까지 온 길에 경사로 놓을 수 있는지
                # 못놓는다 -> break
                ans_h=False
                break
            else:
                # 놓는다 -> 갱신
                val_h = h
                acc_h = 1
        elif val_h > h : #작아짐
            if val_h-h >=2:
                ans_h = False
                break
            if check_h :
                check_h = False
                ans_h = False
                break
            # print("small")
            #여기부터 누적시작
            val_h = h
            check_h = True
            acc_h = 1
        else:#높이 변화 없음
            # print("come")
            acc_h +=1
    if check_h and acc_h ==l :
        check_h = False
    if check_h or not ans_h : #마지막 체크
        # print("i",i,acc_h)
        answer-=1


    for v in ver[1:]:
        if check_v and acc_v ==l :
            check_v = False
            acc_v = 0
        if val_v < v : # 커짐
            if v-val_v >=2:
                ans_v = False
                break
            if check_v :
                check_v = False
                ans_v = False
                break
            if acc_v < l:
                ans_v=False
                break
            else:
                val_v = v
                acc_v = 1
        elif val_v > v : #작아짐
            if val_v -v >=2:
                ans_v = False
                break
            if check_v :

                check_v = False
                ans_v = False
                break
            val_v = v
            check_v = True
            acc_v = 1
        else:#같을 때

            acc_v +=1
    if check_v and acc_v ==l :
        check_v = False
    if check_v or not ans_v : #마지막 체크
        answer-=1

print(answer)