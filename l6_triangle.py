def solution(A):
    A.sort()
    A_positive = [i for i in A if i>0]
    for i in range(len(A_positive)-2):
        if A_positive[i] + A_positive[i+1] > A_positive[i+2]:
            return 1
    return 0
