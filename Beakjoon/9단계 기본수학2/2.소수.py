m = int(input())
n = int(input())

ls = []
for i in range(m, n+1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            ls.append(i)

if len(ls) > 0:
    print(sum(ls))
    print(min(ls))
else:
    print(-1)