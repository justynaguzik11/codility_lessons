def solution(A):
    A_single_values = set(A)
    smallest_int = 1
    for elem in sorted(A_single_values):
        if elem > 0:
            if elem == smallest_int:
                smallest_int+=1
            else:
                return smallest_int
    return smallest_int