"""
날짜 : 2022/02/11
이름 : 강태호
내용 : 코딩테스트 구현 실습
"""
input_date = input()

column = int(ord(input_date[0])) - int(ord('a')) + 1
row = int(input_date[1])

count = 0

if (column + 2) < 9:
    if (row + 1) < 9:
        count += 1
    if 0 < (row - 1):
        count += 1

if(0 < (column-2) and (column-2) < 9):
    if (0 < (row + 1) or (row + 1) < 9):
        count += 1
    if (0 < (row - 1) or (row - 1) < 9):
        count += 1
if(0 < (row+2) and (row+2) < 9):
    if (0 < (column + 1) or (column + 1) < 9):
        count += 1
    if (0 < (column - 1) or (column - 1) < 9):
        count += 1
if(0 < (row-2) and (row-2) < 9):
    if (0 < (column + 1) or (column + 1) < 9):
        count += 1
    if (0 < (column - 1) or (column - 1) < 9):
        count += 1


print(count)
