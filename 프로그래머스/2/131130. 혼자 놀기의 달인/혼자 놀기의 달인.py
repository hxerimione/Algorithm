def solution(cards):
    cards = [0] + cards
    answer = 0
    visit =[0]*(len(cards)+1)
    group=[]
    def find(idx,card,cnt):
        visit[idx] =1
        if visit[card] ==0 :
            return find(card,cards[card],cnt+1)
        else:
            return cnt
    for i,card in enumerate(cards):
        if i>0 and visit[i] ==0 :
            # print(i)
            group.append(find(i,card,1))
    if len(group) <=1 :
        return 0
    group.sort(reverse=True)
    answer=group[0]*group[1]
    return answer