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


"""
import sys

input = sys.stdin.readline


def win_check(line: str, o_cnt: int, x_cnt: int) -> bool:
    # win case
    win = []
    for i in range(3):
        # 가로줄 빙고
        if line[i * 3] != "." and line[i * 3] == line[i * 3 + 1] == line[i * 3 + 2]:
            if line[i * 3] == "X":
                # print(1)
                win.append("X")
            else:
                # print(2)
                win.append("O")
        # 세로줄 빙고
        if line[i] != "." and line[i] == line[i + 3] == line[i + 6]:
            if line[i * 3] == "X":
                # print(3)
                win.append("X")
            else:
                # print(4)
                win.append("O")
    # 대각선 빙고
    if line[4] != "." and (
        line[0] == line[4] == line[8] or line[2] == line[4] == line[6]
    ):
        if line[4] == "X":
            # print(5)
            win.append("X")
        elif line[4] == "O":
            # print(6)
            win.append("O")
    # 만약 빙고가 1개이면
    if len(win) == 1:
        # O로 빙고면 숫자가 같아야함
        if win[0] == "O" and o_cnt == x_cnt:
            # print(7)
            return True
        # X로 빙고면 x가 하나 더 많아야함
        if win[0] == "X" and x_cnt - o_cnt == 1:
            # print(8)
            return True
    # 빙고가 없을 때 x와 o의 개수차가 1이고 .이 없을 때 True
    elif len(win) < 1 and x_cnt - o_cnt == 1 and line.count(".") == 0:
        # print(9)
        return True
    # 빙고가 여러개면 무조건 False
    return False


def tictactoe(line: str, o_cnt: int, x_cnt: int) -> bool:
    # o의 개수는 5개 미만, x의 개수는 6개 미만이어야 하고, o의 개수는 x보다 클수 없음
    if (
        o_cnt < 5
        and x_cnt < 6
        and (abs(x_cnt - o_cnt) <= 1)
        and o_cnt <= x_cnt
        and win_check(line, o_cnt, x_cnt)
    ):
        return True
    return False


def solution():
    while True:
        line = input().strip()
        o_cnt = line.count("O")
        x_cnt = line.count("X")
        if line == "end":
            break
        # 마지막이 가능하면 valid 아니면 invalid
        print("valid") if tictactoe(line, o_cnt, x_cnt) else print("invalid")


if __name__ == "__main__":
    solution()

"""
""" 예외
. X X
X . X
OOO


OXO
XOX
OXX

XXO
XOO
OXX

OXX
OOX
OXX

XXOXOXOO.

OOX
XOO
XXO

XXX
XOO
OXO

XXOXOXOOX

XOOX.OXXO
OXO
XOO
XXX

.XX
X.X
OOO

XXX
XXX
XXX

OXXOOOXXX

OXX
OOO
XXX

XXO
OXX
OOX

XXX
OOX
OOX

XXX
OOX
OOX

XXO
OOX
XOX


.XX
X.X
OOO
"""
