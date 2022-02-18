# n = int(input())
# array = list(map(int, input().split('')))
# cnt = 0
# sosu = 0
#
# for i in array:
#     if i == 1:
#         continue
#     for j in range(2, n+1):
#         if i % j == 0:
#             cnt += 1
#     if cnt == 1:
#         sosu += 1
#
# print(sosu)



n = int(input())
nums = map(int, input().split())
sosu = 0

for i in nums:
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            sosu += 1

print(sosu)
