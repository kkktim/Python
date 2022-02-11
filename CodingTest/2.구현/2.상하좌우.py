"""
날짜 : 2022/02/11
이름 : 강태호
내용 : 코딩테스트 구현 실습
"""

n = int(input())
x, y = 1, 1

plans = input().split()
# print(plans)

for i in plans:

    if(i == "L"):
        y -= 1
        if(y <= 0):
            y += 1
    elif(i == "R"):
        y += 1
        if(y > n):
            y -= 1
    elif(i == "U"):
        x -= 1
        if(x <= 0):
            x += 1
    else:
        x += 1
        if(x > 5):
            x -= 1

print(x, y)