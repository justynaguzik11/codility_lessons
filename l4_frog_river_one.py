def solution(X, A):
    if len(A)<X:
        return -1
    leaf_path = set()
    for index,leaf in enumerate(A):
        leaf_path.add(leaf)
        if len(leaf_path) == X:
            return index
    return -1