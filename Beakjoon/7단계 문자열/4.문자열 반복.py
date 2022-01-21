t = int(input())

for i in range(t):
    r, s = list(map(str, input().split()))
    r = int(r)
    for j in s:
        rs = j*r
        print(rs, end='')
    print()