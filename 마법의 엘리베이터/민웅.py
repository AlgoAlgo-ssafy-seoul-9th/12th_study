ans = float('inf')
def bt(sto, score):
    global ans
    
    if sto < 10:
        score1 = score + int(sto)
        score2 = score + (11-int(sto))
        ans = min(ans, score1, score2)
        return
    
    if score >= ans:
        return
    temp = sto % 10
    
    sto //= 10
    bt(sto+1, score+(10-temp))
    bt(sto, score+temp)
    
    

def solution(storey):
    global ans
    
    bt(storey, 0)
      
    return ans