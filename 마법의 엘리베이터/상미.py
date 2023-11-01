def solution(storey):
    answer = 0
    while storey:
        val = storey % 10
        if (storey//10)%10 >= 5:
            if val >= 5:
                storey = storey+(10-val)
                answer += 10-val
            else:
                storey = storey-val
                answer += val
            storey = storey//10
        else:
            if val > 5:
                storey = storey+(10-val)
                answer += 10-val
            else:
                storey = storey-val
                answer += val
            storey = storey//10
    return answer