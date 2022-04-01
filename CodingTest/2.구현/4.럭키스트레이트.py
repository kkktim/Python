n = input()

ln = []

# print(ln)

mid = len(n) // 2
left_sum = 0
right_sum = 0

for i in n:
    ln.append(i)

for j in ln[:mid]:
    left_sum += int(j)
for k in ln[mid:]:
    right_sum += int(k)

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')



#     if i <= mid:
#         left_sum += int(i)
#     elif int(i) > mid:
#         right_sum += int(i)
#
# if left_sum == right_sum:
#     print('LUCKY')
# else:
#     print('READY')



