from collections import defaultdict
def solution(phone_book):
    answer = True
    phone_book.sort()
    d = defaultdict(int)
    s = set(phone_book)
    if len(s) < len(phone_book):
        return False
    for pb in phone_book : 
        d[pb] += 1
        for i in range(len(pb)):
            if d[pb[:i]] >0 :
                return False
            
    return answer