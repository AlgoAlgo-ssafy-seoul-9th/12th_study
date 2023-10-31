def solution(storey:int) -> int:
    answer = 0
    while storey:
        one = storey % 10 
        if one > 5:
            answer += 10 - one
            storey += 10
        elif one < 5:
            answer += one
        else:
            ten = (storey // 10) % 10
            if ten >= 5:
                answer += 10 - one
                storey += 10
            elif ten < 5:
                answer += one

                
        storey //= 10
    return answer