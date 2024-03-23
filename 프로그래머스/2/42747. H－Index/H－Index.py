def solution(citations):
    answer = 0
    if min(citations) >= len(citations):
        return len(citations)
    citations.sort(reverse=True)
    for i in range(len(citations)-1):
        if citations[i] >= i+1 and citations[i+1] <=i+1 :
            answer=i+1
    return answer