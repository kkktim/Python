"""
날짜 : 2022/02/04
이름 : 강태호
내용 : 코딩테스트 그리디 알고리즘 실습
"""

n, m = map(int, input().split())
dataset = []
result = []

for i in range(n):
    dataset = set(list(input().split()))
    dataset = list(dataset)
    result.append(min(dataset))

print(max(result))