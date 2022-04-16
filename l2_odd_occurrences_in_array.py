def solution(A):
    A.sort()
    odd = A[0::2]
    even = A[1::2]
    for index in range(len(even)):
        if even[index] != odd[index]:
            return odd[index]
    return odd[-1]


if __name__ == '__main__':
    print(solution([1]))
    print("----------------")
    print(solution([1, -2, 3, 3, 1]))