n = int(input())
1 <= n <= 100

for i in range(1, n+1):
    print(' '*(n-i) + '*'*i)