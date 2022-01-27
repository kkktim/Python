dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
tel = list(input())

rs = 0

for i in tel:
    for j in dial:
        if i in j:
            rs += dial.index(j) + 3

print(rs)
