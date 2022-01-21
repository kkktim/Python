c = int(input())

for i in range(c):
    ln = []
    ln = list(map(int, input().split()))
    avg = sum(ln[1:])/ln[0]
    cnt = 0
    for j in ln[1:]:
        if(avg < j):
            cnt += 1
    per = cnt / ln[0] * 100

    print("%.3f" % per + "%")
