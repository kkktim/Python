n, m = map(int, input().split())
ls = list(map(int, input().split()))
# print(ls)

start = 0
end = max(ls)
namuji = 0

while start <= end:
    mid = (start + end) // 2
    namuji_sum = 0
    for i in ls:
        if i > mid:
            namuji = i - mid
            namuji_sum += namuji

    if namuji_sum == m:
        break

    elif namuji_sum < m:
        end = mid - 1
    else:
        start = mid + 1

print(mid)