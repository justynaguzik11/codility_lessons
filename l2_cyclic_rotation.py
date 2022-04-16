def solution(A, K):
    if len(A) == 0 or K == 0 or K == len(A):
        return A
    elif K > len(A):
        K = K % len(A)
    return A[len(A)-K:] + A[0:len(A)-K]


if __name__ == '__main__':
    print(solution([1, 2, 3, 4], 5))
    print("----------------")
    print(solution([1, 2, 3, 4], 1))
    print("----------------")
    print(solution([1, 2, 3, 4], 2))
    print("----------------")
    print(solution([], 1))
