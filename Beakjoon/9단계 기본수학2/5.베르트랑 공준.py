n = int(input())
ls = []

for i in range(n+1, (n*2)+1):
    cnt = 0

    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break

    if cnt == 0:
        ls.append(i)

print(len(ls))

