def solution(A):
    occurences = {el: 0 for el in set(A)}
    for el in A:
        occurences[el] = occurences[el]+ 1
        if occurences[el] > len(A)/2:
            return A.index(el)
    return -1

def solution(A):
    occurences = {}
    for el in A:
        occurences[el] = occurences.get(el, 0) + 1
        if occurences[el] > len(A)/2:
            return A.index(el)
    return -1
