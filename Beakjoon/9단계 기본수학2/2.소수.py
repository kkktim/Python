m = int(input())
n = int(input())

cnt = 0
ls = []
for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
        if cnt == 0:
            ls.append(i)

tot = 0
for k in ls:
    if len(ls) == 0:
        print(-1)
        break
    else:
        tot += k
        print(tot)
        print(min(ls))
