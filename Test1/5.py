"""
날짜 : 2022/01/04
이름 : 강태호
내용 : 1+(1+2)+(1+2+3)+(1+2+3+4)+ ... + (1+2+3+...+10)의 결과를 계산하시오.
"""

sum = 0

for i in range(1, 11):

    for j in range(1, 1+i):
        sum += j
        print('%d' % j, end='+')

    print()

print('총합 :', sum)
