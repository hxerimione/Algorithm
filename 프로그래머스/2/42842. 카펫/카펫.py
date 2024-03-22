def solution(brown, yellow):
    answer = []
    gop = brown+yellow
    hap = (brown+4)//2
    width=1
    while width>0:
        if width*(hap-width)== gop:
            answer = [max(hap-width,width),min(hap-width,width)]
            break
        width+=1
    return answer