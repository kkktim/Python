natnum = set(range(1, 10001))
ln = set()

for i in range(1, 10001):

    for j in str(i):
        i += int(j)
    ln.add(i)

self_num = sorted(natnum - ln)
for s in self_num:
    print(s)



