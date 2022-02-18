# n = int(input())
# array = [5, 3]
# bong = 0
# for i in array:
#     bong += n // i
#     n = n % i
# if n == 0:
#     print(bong)
# else:
#     print(-1)
#

n = int(input())

bong = 0

while n >= 0:
    if n % 5 == 0:
        bong += n // 5
        print(bong)
        break
    n -= 3
    bong += 1
else:
    print(-1)