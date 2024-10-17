from collections import deque,defaultdict
import heapq
def solution(genres, plays):
    answer = []
    dic = defaultdict(int)
    dic_play= defaultdict(list)
    q = []
    for i in range(len(genres)):
        dic[genres[i]] += plays[i]
        if len(dic_play[genres[i]]) ==2 :
            tmp = heapq.heappop(dic_play[genres[i]])
            if plays[i] > tmp[0] : 
                heapq.heappush(dic_play[genres[i]],(plays[i],-i))
            else:
                heapq.heappush(dic_play[genres[i]],tmp)
        elif len(dic_play[genres[i]]) <2 :
            heapq.heappush(dic_play[genres[i]],(plays[i],-i))
            # dic_play[genres[i]].append((plays[i],i))
    new_dic = sorted(dic.items(),key = lambda x:x[1],reverse=True)
    # print(new_dic)
    # print(dic_play)
    for g in new_dic : 
        if len(dic_play[g[0]])==2:
            tmp1 = heapq.heappop(dic_play[g[0]])
            tmp2 = heapq.heappop(dic_play[g[0]])
            answer.append(-tmp2[1])
            answer.append(-tmp1[1])
        else:
            tmp1 = heapq.heappop(dic_play[g[0]])
            answer.append(-tmp1[1])
    return answer