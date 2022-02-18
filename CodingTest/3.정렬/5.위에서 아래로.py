"""
    날짜 : 2022/02/18
    이름 : 강태호
    내용 : 코딩테스트 정렬 실습하기
"""

n = int(input())
array = []

for i in range(n):
    a = int(input())
    array.append(a)

array.sort(reverse=True)
print(array)


