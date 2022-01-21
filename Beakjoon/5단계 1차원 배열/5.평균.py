N = int(input())
score = list(map(int, input().split()))
mscore = max(score)

arr = []
for i in score:
    arr.append(i/mscore*100)

avg = sum(arr) / N
print(avg)