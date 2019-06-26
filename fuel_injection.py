
def solution(n):
    # Your code here
    n = long(n)
    count = 0
    # simple greedy
    while n > 1:
        # divide by 2 if even
        if n & 1 == 0:
            n = n / 2
        else: # go to the nearest multiple of 4
            if n % 4 == 1 or n == 3:
                n = n - 1
            else:
                n += 1
        count += 1
    return count


print(solution(22))
