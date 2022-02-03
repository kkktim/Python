n = int(input())
num = 0
r = 1
cnt = 1

while n > r:
    cnt += 1
    num += 6
    r += num
print(cnt)


# 숫자 [1] [2-7] [8-19] [20-37] [38-61]
# 방 개수 1개 6개 12개 18개 24개
# 지난 수 1개 2개  3개 4개  5개
#
# 1 7 19 37 61
#  6 12 18 24
#   6  6  6

# n = int(input())
# r = 0
# r += 1
# while n > r:
#     if n == r:
#         print("dd")
#     else:
#         print("aa")