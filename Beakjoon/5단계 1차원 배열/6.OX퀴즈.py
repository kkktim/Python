t = int(input())


for i in range(t):
    arr = list(input())
    num = 0
    snum = 0
    for j in arr:
        if(j == 'O'):
            num += 1
            snum += num
        else:
            num = 0

    print(snum)
