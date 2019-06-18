

def solution(area):
    # Your code here
    result = []
    i = area
    while i > 0:
        if i * i <= area:
            result.append(i * i)
            area -= i * i
        if i * i > area:
            i -= 1
    return result


solution(15324)
