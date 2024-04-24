import sys
input = sys.stdin.readline
n = int(input())
if n==0:
    print(0)
    exit(0)
def multi_matrix(A,B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0])%1000000 ,(A[0][0]*B[0][1] + A[0][1]*B[1][1])%1000000 ],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%1000000 ,(A[1][0]*B[0][1] + A[1][1]*B[1][1])%1000000 ]
    ]

def fibonacci(matrix,n):
    
    result = [[1,0],[0,1]]
    base = matrix
    while n>0:
        if n%2==1:
            result = multi_matrix(result,base)
        base = multi_matrix(base,base)
        n //=2
    return result

arr = [[1,1],[1,0]]
result = fibonacci(arr,n-1)
print(result[0][0])



    