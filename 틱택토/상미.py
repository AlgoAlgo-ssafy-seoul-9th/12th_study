
three = [[0,1,2], [3,4,5], [6,7,8], [0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

while True:
    answer = 'valid'
    arr = input()
    if arr == 'end':
        break
    x = arr.count('X')
    o = arr.count('O')
    # 9칸 모두 찼으면
    if x+o == 9:
        if x != 5:
            answer = 'invalid'
    # 9칸 안 찼으면
    else:
        if x-o <= 1:
            index_x = []
            index_o = []
            for i in range(9):
                if arr[i] =='O':
                    index_o.append(i)
                else:
                    index_x.append(i)
            if x > o:
                if index_o in three:
                    answer = 'invalid'
            elif x == o:
                if index_x not in three and index_o not in three:
                    answer = 'invalid'
            else:
                answer = 'invalid'
        else:
            answer = 'invalid'
    print(answer)

