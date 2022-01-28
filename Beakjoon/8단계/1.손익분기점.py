a, b, c = map(int, input().split())

if b >= c :
    print(-1)
else:
    x = a // (c - b)
    print(x+1)


# print(a)
# print(b)
# print(c)

# a + (b * x) = c * x
#
# a + bx = cx
# a = cx - bx
# a = x(c-b)
# a/(c-b) = x