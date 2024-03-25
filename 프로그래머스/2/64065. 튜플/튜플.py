from collections import defaultdict
def solution(s):
    answer=[]
    dict = defaultdict(int)
    s=s.replace('{',' ').replace('}',' ')
    arr= s.split()
    for a in arr:
        if a==',':
            continue
        else:
            answer.append(a.split(','))
    for a in answer:
        for n in a :
            dict[n] +=1

    answer = [0 for _ in range(len(dict))]
    for k,v in dict.items() :
        answer[len(dict)-v] = int(k)
    return answer