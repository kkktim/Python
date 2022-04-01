n = int(input())
gong = list(map(int, input().split()))
# print(gong)
gong.sort()
mohum = 0
grr = 0

for i in gong:
    mohum += 1
    if i <= mohum:
        grr += 1
        mohum = 0

print(grr)