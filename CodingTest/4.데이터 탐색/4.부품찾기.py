from bisect import bisect_left

n = int(input())
ls = []
ls = list(map(int, input().split()))
m = int(input())
prod_ls = []
prod_ls = list(map(int, input().split()))
ls.sort()

def binary_search(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target:
        return i
    else:
        return -1

# pos = binary_search(ls, 9)
# print(pos)

for j in prod_ls:
    pos = binary_search(ls, j)
    if pos == -1:
        print('no', end=' ')
    else:
        print('yes', end=' ')


# print(ls)
# print(prod_ls)