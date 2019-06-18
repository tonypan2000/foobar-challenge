from itertools import combinations


def solution(l):
    # Your code here
    l.sort(reverse=True)
    for i in reversed(range(1, len(l) + 1)):
        for combo in combinations(l, i):
            if sum(combo) % 3 == 0:
                return int(''.join(map(str, combo)))
    return 0


L = [3, 1, 4, 1, 5, 9]
print(solution(L))
