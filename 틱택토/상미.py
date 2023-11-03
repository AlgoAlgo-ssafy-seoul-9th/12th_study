three = [[0,1,2], [3,4,5], [6,7,8], [0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

while True:
    answer = 'valid'
    arr = input()
    if arr == 'end':
        break
    x = arr.count('X')
    o = arr.count('O')
    index_x = []
    index_o = []
    for i in range(9):
        if arr[i] =='O':
            index_o.append(i)
        elif arr[i] =='X':
            index_x.append(i)
            
    # 9칸 모두 찼으면
    if x+o == 9:
        if x != 5:
            answer = 'invalid'
        else:
            for t in three:
                cnt = 0
                for num in t:
                    if num in index_o:
                        cnt += 1
                if cnt == 3:
                    answer = 'invalid'

    # 9칸 안 찼으면
    else:
        if x-o <= 1:
            if x > o:
                for t in three:
                    cnt_o = 0
                    cnt_x = 0
                    for num in t:
                        if num in index_o:
                            cnt_o += 1
                        if num in index_x:
                            cnt_x += 1
                    # o가 빙고가 되어있는 상태면 안 됨
                
                    if cnt_x == 3 and cnt_o != 3:
                        answer = 'valid'
                    else:
                        answer = 'invalid'
            elif x == o:
                for t in three:
                    cnt_o = 0
                    cnt_x = 0
                    for num in t:
                        if num in index_o:
                            cnt_o += 1
                            if cnt_o ==3:
                                break
                        if num in index_x:
                            cnt_x += 1
                            if cnt_x ==3:
                                break
                    if cnt_o != 3 and cnt_x ==3:
                        answer = 'invalid'
            else:
                answer = 'invalid'
        else:
            answer = 'invalid'
    print(answer)

