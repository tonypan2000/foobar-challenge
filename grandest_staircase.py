def solution(n):
    # Your code here
    # DP, 2D list of 0s
    memo = [[0 for i in range(n + 1)] for j in range(n + 1)]
    memo[0][0] = 1
    for lower in range(1, n + 1):
        for left in range(0, n + 1):
            memo[lower][left] = memo[lower - 1][left]
            if left >= lower:
                memo[lower][left] += memo[lower - 1][left - lower]
    return memo[n][n] - 1


print(solution(200))
print(solution(3))
print(solution(4))
print(solution(5))