def solution(l, t):
    # Your code here
    for i in range(len(l)):
        for j in range(i, len(l)):
            if sum(l[i:j + 1]) == t:
                return [i, j]
    return [-1, -1]


t1 = [1, 2, 3, 4]
t2 = [4, 3, 10, 2, 8]
t3 = [1, 2, 3]
print(solution(t1, 15))
print(solution(t2, 12))
print(solution(t3, 6))