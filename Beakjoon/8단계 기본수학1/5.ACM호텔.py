t = int(input())
floor = 0
num = 0

for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    num = n // h + 1
    if n % h == 0:
        num = n // h
        floor = h
    print(f'{floor*100+num}')



# t = int(input())
#
# cnt = 0
#
# for i in range(t):
#     h, w, n = map(int, input().split())
#     for j in range(1, w):
#         for k in range(h):
#             cnt += 1
#             if (n == cnt):
#                 if(j < 10):
#                     rs1 = (str(k+1)+'0'+str(j))
#                 else:
#                     rs2 = print(str(k+1)+str(j))


