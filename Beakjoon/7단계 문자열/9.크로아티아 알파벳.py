cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

c = input()

for i in cro:
    c = c.replace(i, '*')

print(len(c))

