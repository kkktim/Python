# m, n = map(int, input().split())
#
# for i in range(m, n+1):
#     if i > 0:
#         cnt = 0
#         for j in range(2, i):
#             if i % j == 0:
#                 cnt += 1
#                 break
#         if cnt == 0:
#             print(i)
#
def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)