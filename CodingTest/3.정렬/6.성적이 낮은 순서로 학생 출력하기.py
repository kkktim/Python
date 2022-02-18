"""
    날짜 : 2022/02/18
    이름 : 강태호
    내용 : 코딩테스트 정렬 실습하기
"""

n = int(input())
dict = {}
for i in range(n):
    a, b = input().split()
    dict[a] = b
    # print(dict)

#람다식으로 value값 기준으로 오름차순 정렬 후 key값을 리스트에 저장
dict2 = sorted(dict.items(), key=lambda data:data[1])
array = []
for j in range(len(dict2)):
    array.append(dict2[j][0])

print(array)




