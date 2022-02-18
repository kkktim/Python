# a, b = map(int, input().split())
# c = int(input())

# hour = 0
# minute = 0
#
# if b + c >= 60:
#     minute = (b+c) - 60
#     hour = a + 1
#     if hour > 23:
#         hour = 0
# if b + c < 60:
#     minute = b+c
#     hour = a
#     if hour > 23:
#         hour = 0
#
# print(hour, minute)

h, m = map(int, input().split())
timer = int(input())

h += timer // 60
m += timer % 60

if m >= 60:
    h += 1
    m -= 60
if h > 23:
    h -= 24

print(h, m)
