def solution(S):
    if S == "":
        return 1
    n = len(S)
    parity = lambda a: a % 2
    if parity(n) == 1:
        return 0

    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}
    for character in S:
        if character in pairs.keys():
            stack.append(character)
        if character in pairs.values():
            if stack == []:
                return 0
            opening = stack[-1]
            if character == pairs[opening]:
                stack.pop()
            else:
                return 0
    if stack != []:
        return 0
    return 1


if __name__ == '__main__':
    print(solution('[(])'))
    print(solution('()()[]{[()()]{}}'))