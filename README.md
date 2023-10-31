# 12th_study

알고리즘 스터디 12주차

[백준 문제집](https://www.acmicpc.net/workbook/view/17214) <br/>
[프로그래머스](https://school.programmers.co.kr/learn/courses/30/lessons/148653)

# [마법의 엘리베이터]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](<./마법의 엘리베이터/민웅.py>)

```py
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
    
    # 성구 수정
    sto //= 10
    bt(sto+1, score+(10-temp))
    bt(sto, score+temp)
    
    

def solution(storey):
    global ans
    
    bt(storey, 0)
      
    return ans

```

### [병국](<./마법의 엘리베이터/병국.py>)

```py

```

### [상미](<./마법의 엘리베이터/상미.py>)

```py

```

### [서희](<./마법의 엘리베이터/서희.py>)

```py

```

### [성구](<./마법의 엘리베이터/성구.py>)

```py
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
```

</div>

</details>

<br><br>

# 틱택토

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./틱택토/민웅.py)

```py
# 7682_틱택토_tiktakto
import sys
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

while True:
    game = input().strip()
    if game == 'end':
        break

    line1 = game[:3]
    line2 = game[3:6]
    line3 = game[6:]
    game = []
    game.append(list(line1))
    game.append(list(line2))
    game.append(list(line3))

    cnt_x = 0
    cnt_o = 0
    is_x = 0
    is_o = 0
    for i in range(3):
        for j in range(3):
            now = game[i][j]

            if now == 'X':
                cnt_x += 1
            elif now == 'O':
                cnt_o += 1

            if now != '.':
                for d in dxy:
                    x = i
                    y = j
                    check = 1
                    while True:
                        x = x + d[0]
                        y = y + d[1]
                        if check == 3:
                            if now == 'X':
                                is_x += 1
                            else:
                                is_o += 1

                        if 0 <= x <= 2 and 0 <= y <= 2:
                            if game[x][y] == now:
                                check += 1
                                continue
                        else:
                            break

    if is_x and is_o:
        print('invalid')
        continue

    if is_x and cnt_x != (cnt_o+1):
        print('invalid')
        continue

    if is_o and cnt_x != cnt_o:
        print('invalid')
        continue

    if abs(cnt_o - cnt_x) >= 2:
        print('invalid')
        continue

    if cnt_x < cnt_o:
        print('invalid')
        continue

    if is_o and cnt_x > cnt_o:
        print('invalid')
        continue

    if (cnt_x + cnt_o) != 9 and not is_x and not is_o:
        print('invalid')
        continue

    print('valid')

```

## [병국](./틱택토/병국.py)

```py


def make(aa):
    new_arr = []
    for i in range(0,8,3):
        arr = list(aa[i:i+3])
        new_arr.append(arr)
    return new_arr


# O가 이겼는데 X 가 더 많은 상황은안됨
def checkend(aa, OorX):
    global check_o
    flag = 'valid'
    check = False
    if aa[0]==aa[3]==aa[6] == OorX:
        return True
    if aa[0] == aa[4] == aa[8]== OorX:
        return True
    if aa[0] == aa[1] == aa[2]== OorX:
        return True
    if aa[1] == aa[4] == aa[7]== OorX:
        return True
    if aa[2] == aa[4] == aa[6]== OorX:
        return True
    if aa[3] == aa[4] == aa[5]== OorX:
        return True
    if aa[6] == aa[7] == aa[8]== OorX:
        return True
    if aa[2] == aa[5] == aa[8]== OorX:
        return True
    return False


for i in range(100000):
    check_o = ''
    plus = 0
    minus = 0
    blank = 0
    aa = input()
    if aa == 'end':
        break
    else:
        for i in range(len(aa)):
            if aa[i] == 'X':
                plus += 1
            elif aa[i] == 'O':
                minus += 1
            else:
                blank += 1
        if plus - minus > 1:
            print('invalid')
            continue
        if minus > plus:
            print('invalid')
            continue
        if plus==5 and minus==4:
            if not checkend(aa,'O'):
                print('valid')
                continue
        if plus == minus: # 개수 같으면 X가아니라 O가 끝낸다
            if checkend(aa,'O') and not checkend(aa,'X'):
                print('valid')
                continue
        if plus-1 == minus: # 이건 X가 이긴다
            if checkend(aa,'X') and not checkend(aa,'O'):
                print('valid')
                continue
        print('invalid')



```

## [상미](./틱택토/상미.py)

```py

```

## [서희](./틱택토/서희.py)

```py

```

## [성구](./틱택토/성구.py)

```py
# 7682 틱택토
import sys

input = sys.stdin.readline


def check(line: str, S: str) -> bool:
    for i in range(3):
        # 세로 체크
        if line[i] == line[i + 3] == line[i + 6] == S:
            return True
        # 가로 체크
        if line[i * 3] == line[i * 3 + 1] == line[i * 3 + 2] == S:
            return True
    # 대각선 체크
    if line[0] == line[4] == line[8] == S or line[2] == line[4] == line[6] == S:
        return True
    return False


def solution(line: str, o_cnt: int, x_cnt: int) -> bool:
    if x_cnt > o_cnt + 1 or o_cnt > x_cnt:
        return False
    # 3가지 이외에는 종료될 수가 없음
    if o_cnt == x_cnt and check(line, "O") and not check(line, "X"):
        return True
    if o_cnt + 1 == x_cnt and check(line, "X") and not check(line, "O"):
        return True
    if o_cnt == 4 and x_cnt == 5 and not check(line, "O"):
        return True
    return False


if __name__ == "__main__":
    while True:
        line = input().strip()
        # 갯수 체크
        o_cnt = line.count("O")
        x_cnt = line.count("X")
        if line == "end":
            break
        # 마지막이 가능하면 valid 아니면 invalid
        print("valid") if solution(line, o_cnt, x_cnt) else print("invalid")

```

</div>

</details>

<br><br>

# 등산마니아

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./등산마니아/민웅.py)

```py


```

## [병국](./등산마니아/병국.py)

```py

```

## [상미](./등산마니아/상미.py)

```py

```

## [서희](./등산마니아/서희.py)

```py

```

## [성구](./등산마니아/성구.py)

```py

```

</div>

</details>
