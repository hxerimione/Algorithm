def solution(elements):
    answer = 0
    s=set()
    arr=[]
    for e in elements:
        arr.append(e)
        s.add(e)

    for i in range(1,len(elements)):
        for k in range(len(elements)):
            arr[k] += elements[(k+i)%len(elements)]
            s.add(arr[k])


    return len(s)