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

```

</div>

</details>

<br><br>

# 틱택토

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./틱택토/민웅.py>)

```py

```

## [병국](<./틱택토/병국.py>)

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

## [상미](<./틱택토/상미.py>)

```py

```

## [서희](<./틱택토/서희.py>)

```py

```

## [성구](<./틱택토/성구.py>)

```py

```

</div>

</details>

<br><br>

# 등산마니아

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./등산마니아/민웅.py>)

```py


```

## [병국](<./등산마니아/병국.py>)

```py

```

## [상미](<./등산마니아/상미.py>)

```py

```

## [서희](<./등산마니아/서희.py>)

```py

```

## [성구](<./등산마니아/성구.py>)

```py

```

</div>

</details>

