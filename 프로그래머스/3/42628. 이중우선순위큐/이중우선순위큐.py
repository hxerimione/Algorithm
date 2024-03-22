import heapq

def solution(operations):
    answer = []
    q = []
    for operation in operations :
        if operation == 'D 1': #최댓값 삭제
            if len(q)>0:
                max_val = max(q)
                q.remove(max_val)
        elif operation == 'D -1': #최솟값 삭제
            if len(q)>0:
                heapq.heappop(q)
        else:
            op = operation.split()
            number = int(op[1])
            heapq.heappush(q,number)
        
    if len(q)==0:
        return [0,0]
    return [max(q),min(q)]