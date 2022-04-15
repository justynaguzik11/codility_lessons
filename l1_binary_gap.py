def solution(N):
    binary = ''
    while N > 0:
        binary += str(N % 2)
        N = N // 2
    binary = binary[::-1]
    binary = binary.rstrip('0')
    gaps = binary.split('1')
    return max(len(s) for s in gaps)

if __name__ == '__main__':
    print(solution(1041))
    print("----------------")
    print(solution(1024))
    print("----------------")
    print(solution(6))