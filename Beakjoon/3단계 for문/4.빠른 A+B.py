import sys

t = int(input())
t <= 1000000

for i in range(t):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    1 <= A, B <= 1000
    print( A + B )

