from collections import Counter
def solution(want, number, discount):
    answer = 0
    d = Counter(discount[:10])

    flag = True
    for i in range(len(want)):
        if want[i] in d.keys() and d[want[i]] >= number[i]:
            continue
        else:
            flag=False
            break
    if flag:
        answer+=1

    for i in range(len(discount)):
        d[discount[i]]-=1
        if len(discount)>i+10:
            if discount[i+10] in d.keys():
                d[discount[i+10]]+=1
            else:
                d[discount[i+10]]=1

        flag = True
        for j in range(len(want)):
            if want[j] in d.keys() and d[want[j]] >= number[j]:
                continue
            else:
                flag=False
                break
        if flag:
            answer+=1
    return answer