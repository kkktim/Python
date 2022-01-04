"""
날짜 : 2022/01/03
이름 : 강태호
내용 : 파이썬 3장 연습문제 교재 p77
"""

"""[문제1]"""
"""[문제2 '숫자 맞추기 게임']"""
import random

print('숫자 맞추기 게임')
com = random.randint(1, 10)

while True:
    my = int(input('예상 숫자를 입력하시오 :'))

    if my > com:
        print('더 작은 수 입력')
        continue

    if my < com:
        print('더 더 큰 수 입력')
        continue

    if my == com:
        break

print('~~ 성공 ~~')
