"""
날짜 : 2022/02/04
이름 : 강태호
내용 : 코딩테스트 그리디 알고리즘 실습
"""

n, k = map(int, input().split())

result = 0

while True:
    if n == 1:
        break

    elif n % k != 0:
        n -= 1

    else:
        n /= k

    result += 1

print(result)