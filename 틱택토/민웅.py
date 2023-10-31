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
