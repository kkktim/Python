H, M = map(int, input().split())
0 <= H <= 23
0 <= M <= 59

if (M >= 45):
    M = M - 45
    print(H, M)

elif (M < 45) and (H > 0):
    m = 45 - M
    print(H - 1, 60 - m)

else:
    H = 24
    M = 45 - M
    print(H - 1, 60 - M)
